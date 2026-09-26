"""Add an optional official trailer URL to title overrides.

Revision ID: f7a8b9c0d1e2
Revises: c9d0e1f2a3b4
"""
from alembic import op
import sqlalchemy as sa


revision = 'f7a8b9c0d1e2'
down_revision = 'c9d0e1f2a3b4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('title_overrides', sa.Column('trailer_url', sa.Text(), nullable=True))


def downgrade():
    op.drop_column('title_overrides', 'trailer_url')