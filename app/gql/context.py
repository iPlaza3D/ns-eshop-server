"""Per-request GraphQL context."""
from dataclasses import dataclass
from typing import Optional

from flask_login import current_user

from auth import admin_account_created
from settings import get_settings


@dataclass
class GraphQLContext:
    user: Optional[object]
    can_admin: bool
    can_shop: bool


def build_context(user=None) -> GraphQLContext:
    """Build the GraphQL context for the resolved session or Basic Auth user.

    When no admin user has been provisioned (initial setup) auth is disabled;
    callers are treated as admin/shop to mirror the rest of the API.
    """
    if not admin_account_created():
        return GraphQLContext(user=None, can_admin=True, can_shop=True)
    if user is None and current_user.is_authenticated:
        user = current_user._get_current_object()
    if user is None:
        return GraphQLContext(
            user=None,
            can_admin=False,
            can_shop=get_settings()['shop']['public'],
        )
    return GraphQLContext(
        user=user,
        can_admin=bool(user.has_admin_access()),
        can_shop=bool(user.has_shop_access()) or get_settings()['shop']['public'],
    )


def role_key(ctx: GraphQLContext) -> str:
    """Stable string fed into the ETag so caches don't bleed across roles."""
    if ctx.can_admin:
        return "admin"
    if ctx.can_shop:
        return "shop"
    return "anon"
