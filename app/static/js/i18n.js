(() => {
    'use strict';

    const spanish = {
        'Toggle navigation': 'Abrir navegación',
        'Language': 'Idioma',
        'Library': 'Biblioteca',
        'Library view': 'Vista de biblioteca',
        'NS ESHOP SERVER / LIBRARY': 'NS ESHOP SERVER / BIBLIOTECA',
        'Setup': 'Configuración',
        'Setup Guide': 'Guía de configuración',
        'Admin': 'Administración',
        'Login': 'Iniciar sesión',
        'Logout': 'Cerrar sesión',
        'Your collection': 'Tu colección',
        'The titles tracked by your server, all in one place.': 'Los títulos registrados en tu servidor, en un solo lugar.',
        'GAME DETAILS': 'DETALLES DEL JUEGO',
        'DOWNLOADABLE CONTENT': 'CONTENIDO DESCARGABLE',
        'Loading game...': 'Cargando juego...',
        'Loading game details...': 'Cargando información del juego...',
        'No catalogue entry is linked to this item.': 'Este elemento no tiene una ficha de catálogo asociada.',
        'No catalogue entry was found for this item.': 'No se encontró una ficha de catálogo para este elemento.',
        'Unable to load game details.': 'No se pudo cargar la información del juego.',
        'No description is available for this title.': 'No hay una descripción disponible para este título.',
        'Downloadable content': 'Contenido descargable',
        'No DLC listed in the catalogue.': 'El catálogo no incluye DLC para este juego.',
        'and more...': 'y más...',
        'Your library': 'Tu biblioteca',
        'In library': 'En tu biblioteca',
        'Not in library': 'No está en tu biblioteca',
        'DLC in library': 'DLC en tu biblioteca',
        'DLC missing': 'DLC faltante',
        'Base game in library': 'Juego base en tu biblioteca',
        'Base game missing': 'Falta el juego base',
        'Update missing': 'Falta la actualización',
        'Available updates': 'Actualizaciones disponibles',
        'No update versions listed.': 'No hay versiones de actualización registradas.',
        'Release date unknown': 'Fecha de lanzamiento desconocida',
        'View details for': 'Ver detalles de',
        'Developer': 'Desarrollador',
        'Publisher': 'Distribuidora',
        'Released': 'Lanzamiento',
        'Players': 'Jugadores',
        'Rating': 'Clasificación por edad',
        'Languages': 'Idiomas',
        'Title ID': 'ID del título',
        'Copy Title ID': 'Copiar ID del título',
        'Copied.': 'Copiado.',
        'Copy is unavailable in this browser.': 'Este navegador no permite copiar.',
        'Custom metadata': 'Metadatos personalizados',
        'TitleDB catalogue': 'Catálogo TitleDB',
        'Add to favorites': 'Añadir a favoritos',
        'Remove from favorites': 'Quitar de favoritos',
        'owned': 'en tu biblioteca',
        'Unknown title': 'Título desconocido',
        'Loading library...': 'Cargando biblioteca...',
        'catalogue entries': 'elementos del catálogo',
        'catalogue entry': 'elemento del catálogo',
        'Search titles...': 'Buscar títulos...',
        'Search titles': 'Buscar títulos',
        'Filter library': 'Filtrar biblioteca',
        'Type filter': 'Filtro por tipo',
        'Ownership filter': 'Filtro de propiedad',
        'Update filter': 'Filtro de actualización',
        'Completion filter': 'Filtro de contenido',
        'All': 'Todos',
        'Base': 'Juego base',
        'Owned': 'En biblioteca',
        'Missing': 'Faltante',
        'Up to date': 'Actualizado',
        'Missing Update': 'Falta actualización',
        'Complete': 'Completo',
        'Missing DLC': 'Falta DLC',
        'Card view': 'Vista de tarjetas',
        'Icon view': 'Vista de iconos',
        'List view': 'Vista de lista',
        'Per page': 'Por página',
        'Items per page': 'Elementos por página',
        'Custom': 'Personalizado',
        'Apply': 'Aplicar',
        'Card density': 'Tamaño de tarjetas',
        'Adjust card density': 'Ajustar tamaño de tarjetas',
        'Page navigation': 'Paginación',
        'Previous': 'Anterior',
        'Next': 'Siguiente',
        'titles': 'títulos',
        'complete': 'completos',
        'up to date': 'actualizados',
        'files': 'archivos',
        'Please login to your account': 'Inicia sesión en tu cuenta',
        'Username': 'Usuario',
        'Password': 'Contraseña',
        'Remember me': 'Recordarme',
        'Supported Clients': 'Clientes compatibles',
        'NS eShop Server supports the following Nintendo Switch clients:': 'NS eShop Server es compatible con estos clientes de Nintendo Switch:',
        'Setup Instructions': 'Instrucciones de configuración',
        'Local Access': 'Acceso local',
        'Remote Access': 'Acceso remoto',
        'Tinfoil Setup': 'Configuración de Tinfoil',
        'Sphaira Setup': 'Configuración de Sphaira',
        'CyberFoil Setup': 'Configuración de CyberFoil',
        'Unable to determine local server address. Please check your network configuration.': 'No se pudo determinar la dirección local del servidor. Comprueba la configuración de red.',
        'Remote host not configured.': 'No se ha configurado el host remoto.',
        'Please configure the remote host in the Settings page under the Shop section.': 'Configura el host remoto en la sección Tienda de Ajustes.',
        'HTTP / HTTPS protocol support': 'Compatibilidad con los protocolos HTTP y HTTPS',
        'User authentication': 'Autenticación de usuarios',
        'Shop browsing with icons and banners': 'Exploración de la tienda con iconos y banners',
        'Directory-based file browsing': 'Exploración de archivos por directorios',
        'Compressed content (NSZ and XCZ) support': 'Compatibilidad con contenido comprimido (NSZ y XCZ)',
        'Encrypted shop support': 'Compatibilidad con tiendas cifradas',
        'Custom welcome message (MOTD)': 'Mensaje de bienvenida personalizado (MOTD)',
        'protocol support': 'compatibilidad con los protocolos',
        'Content filtering (games, updates, DLC, XCI) based on URL': 'Filtrado de contenido (juegos, actualizaciones, DLC y XCI) según la URL',
        'New games, DLC, Updates, Recommended and XCI sections': 'Secciones de novedades, DLC, actualizaciones, recomendados y XCI',
        'Client side Host verification for secure connections': 'Verificación del host en el cliente para conexiones seguras',
        'Shop browsing with icons and Sections (Updates, DLC)': 'Exploración de la tienda con iconos y secciones (actualizaciones y DLC)',
        'Local Access is for when your Nintendo Switch and NS eShop Server are on the same network (e.g., both on your home WiFi).': 'El acceso local se usa cuando tu Nintendo Switch y NS eShop Server están en la misma red (por ejemplo, en el WiFi de casa).',
        'Remote Access allows you to access your NS eShop Server shop from anywhere over the internet.': 'El acceso remoto permite entrar a tu tienda NS eShop Server desde cualquier lugar por internet.',
        'allows you to access your NS eShop Server shop from anywhere over the internet. Requires proper port forwarding or a reverse proxy setup.': 'permite entrar a tu tienda NS eShop Server desde cualquier lugar por internet. Requiere configurar el reenvío de puertos o un proxy inverso.',
        'is for when your Nintendo Switch and NS eShop Server are on the same network (e.g., both on your home WiFi).': 'se usa cuando tu Nintendo Switch y NS eShop Server están en la misma red (por ejemplo, en el WiFi de casa).',
        'allows you to access your NS eShop Server shop from anywhere over the internet.': 'permite entrar a tu tienda NS eShop Server desde cualquier lugar por internet.',
        'Requires proper port forwarding or a reverse proxy setup.': 'Requiere configurar correctamente el reenvío de puertos o un proxy inverso.',
        'Please configure the remote host in the': 'Configura el host remoto en',
        'page under the Shop section.': 'dentro de la sección Tienda.',
        'On your Nintendo Switch, open': 'En tu Nintendo Switch, abre',
        'Open': 'Abre',
        'New': 'Nuevo',
        'Menu': 'menú',
        'and': 'y',
        'and turn on': 'y activa la opción',
        'Add': 'Añade',
        'Add new shop': 'Añadir tienda nueva',
        'Ensure': 'Asegúrate de que la',
        'Active shop': 'tienda activa',
        'is set to the correct shop': 'esté seleccionada correctamente',
        'to go back to the main menu, and open': 'para volver al menú principal y abre',
        'Back': 'Atrás',
        'Install from eShop': 'Instalar desde eShop',
        'to browse your shop': 'para explorar la tienda',
        'Navigate to': 'Ve a',
        'Enter the following details:': 'Introduce estos datos:',
        'Press': 'Pulsa',
        'Save': 'Guardar',
        'to save the location and load the shop': 'para guardar la ubicación y cargar la tienda',
        'restart Sphaira': 'reinicia Sphaira',
        'and restart Sphaira': 'y reinicia Sphaira',
        'Opening a file will show a preview of its content. To actually install the file, press Options → Install.': 'Al abrir un archivo verás una vista previa. Para instalarlo, pulsa Opciones → Instalar.',
        'Opening a file will show a preview of its content. To actually install the file, press': 'Al abrir un archivo verás una vista previa. Para instalarlo, pulsa',
        'To refresh the shop, simply select another Mount then select back NS eShop Server.': 'Para actualizar la tienda, selecciona otro montaje y vuelve a elegir NS eShop Server.',
        'To refresh the shop, simply select another': 'Para actualizar la tienda, selecciona otro',
        'then select back': 'y vuelve a seleccionar',
        'then select back NS eShop Server.': 'y vuelve a seleccionar NS eShop Server.',
        'Options': 'Opciones',
        'Install': 'Instalar',
        'Mount': 'Montaje',
        'Select': 'Selecciona',
        'FileBrowser': 'Explorador de archivos',
        'Add / modify mounts': 'Añadir o modificar montajes',
        'Create New Entry': 'Crear entrada nueva',
        'File Browser': 'Explorador de archivos',
        'Advanced Options': 'Opciones avanzadas',
        'Install options': 'Opciones de instalación',
        'Enable emummc': 'emuMMC',
        'Save the location and load the shop': 'Guarda la ubicación y carga la tienda',
        'Ensure Active shop is set to the correct shop': 'Comprueba que la tienda activa sea la correcta',
        'Press Back to go back to the main menu, and open Install from eShop to browse your shop': 'Pulsa Atrás para volver al menú principal y abre Instalar desde eShop para explorar la tienda.',
        'Opening a file will show a preview of its content.': 'Al abrir un archivo verás una vista previa de su contenido.',
        'Unable to determine local server address.': 'No se pudo determinar la dirección local del servidor.',
        'The path is for all content, else one of': 'La ruta sirve todo el contenido; también puedes usar',
        'for': 'para',
        'all': 'todo',
        'content, else one of': 'el contenido; también puedes usar',
        'to serve specific content.': 'para servir contenido específico.',
        'Local': 'Local',
        'Remote': 'Remoto',
        'Open in browser': 'Abrir en el navegador',
        'Protocol:': 'Protocolo:',
        'Host:': 'Host:',
        'Port:': 'Puerto:',
        'Path:': 'Ruta:',
        'Title:': 'Nombre:',
        'Enabled:': 'Activado:',
        'Type:': 'Tipo:',
        'Name:': 'Nombre:',
        'URL:': 'URL:',
        'User:': 'Usuario:',
        'Pass:': 'Contraseña:',
        'Shop title:': 'Nombre de la tienda:',
        'Shop protocol:': 'Protocolo de la tienda:',
        'Username:': 'Usuario:',
        'Password:': 'Contraseña:',
        'All content': 'Todo el contenido',
        'Settings': 'Ajustes',
        'Tasks': 'Tareas',
        'Stats': 'Estadísticas',
        'Authentication': 'Autenticación',
        'Missing admin account!': 'Falta la cuenta de administrador',
        'NS eShop Server requires an admin account to enable authentication. Until an account with admin rights is created,': 'NS eShop Server necesita una cuenta de administrador para activar la autenticación. Hasta que se cree una cuenta con permisos de administrador,',
        'authentication is disabled, anyone can access and change the configuration of your shop!': 'la autenticación estará desactivada y cualquiera podrá acceder a la configuración de la tienda y modificarla.',
        'Add an admin account': 'Añade una cuenta de administrador',
        'here under Authentication': 'en el apartado Autenticación',
        'Missing / invalid console keys file!': 'Falta el archivo de claves de consola o no es válido',
        'Console keys are required to decrypt any Nintendo content, including backups. NS eShop Server uses this to identify files, regardless of the filename.': 'Las claves de consola son necesarias para descifrar contenido de Nintendo, incluidas las copias. NS eShop Server las usa para identificar archivos, independientemente del nombre.',
        'Titles will be missed or misidentified if you don\'t fill in your keys!': 'Si no añades las claves, algunos títulos no se detectarán o se identificarán incorrectamente.',
        'See': 'Consulta',
        'this guide': 'esta guía',
        'on how to extract the keys from your console, and upload them': 'para extraer las claves de tu consola y subirlas',
        'here in NS eShop Server.': 'aquí, en NS eShop Server.',
        'If keys are missing, all files': 'Si faltan las claves, todos los archivos',
        'must contain "[TITLEID][vVERSION]"': 'deben incluir "[TITLEID][vVERSION]"',
        ', else the file won\'t be recognized.': ', o no se podrán identificar.',
        'Missing shop Host!': 'Falta el host de la tienda',
        'Host verification from outside the local network is disabled if the shop': 'La verificación del host desde fuera de la red local está desactivada si el campo',
        'is missing, configure it': 'está vacío; configúralo',
        'to prevent someone else stealing from your shop.': 'para evitar que otra persona use tu tienda.',
        'here in NS eShop Server': 'aquí en NS eShop Server',
        'List of users:': 'Lista de usuarios:',
        'Configure directories containing your games.': 'Configura los directorios que contienen tus juegos.',
        'Add library path': 'Añadir ruta de biblioteca',
        'Scan library': 'Analizar biblioteca',
        'Add a new directory:': 'Añadir un directorio:',
        'Delete library path': 'Eliminar ruta de biblioteca',
        'File watcher': 'Monitor de archivos',
        'Monitor library paths for changes. Local paths use native OS events; network filesystems are polled at the interval below.': 'Supervisa los cambios en las rutas de biblioteca. Las rutas locales usan eventos del sistema; los sistemas de archivos de red se consultan con el intervalo indicado.',
        'Enable file watcher': 'Activar monitor de archivos',
        'Polling interval': 'Intervalo de consulta',
        'Management': 'Gestión',
        'Configure automated library management.': 'Configura la gestión automática de la biblioteca.',
        'Delete older updates': 'Eliminar actualizaciones antiguas',
        'Deletes older update files when a newer version is available in the library.': 'Elimina archivos de actualización antiguos cuando la biblioteca contiene una versión más reciente.',
        'File compression': 'Compresión de archivos',
        'Compress files to save disk space after they are added and organized.': 'Comprime los archivos para ahorrar espacio después de añadirlos y organizarlos.',
        'Compress files': 'Comprimir archivos',
        'Compress files to': 'Comprimir archivos a',
        'after they are added and organized. Every compressed file is verified before the original is removed.': 'después de añadirlos y organizarlos. Se verifica cada archivo comprimido antes de eliminar el original.',
        'Compression level': 'Nivel de compresión',
        'Higher = smaller files but slower. Default:': 'Un nivel mayor genera archivos más pequeños, pero tarda más. Valor predeterminado:',
        'Advanced compression options': 'Opciones avanzadas de compresión',
        'Long-distance mode': 'Modo de larga distancia',
        'Compression mode:': 'Modo de compresión:',
        'Block size exponent:': 'Exponente del tamaño de bloque:',
        'Threads per file:': 'Hilos por archivo:',
        'File verification': 'Verificación de archivos',
        'Check that files are original and intact. Requires valid console keys.': 'Comprueba que los archivos sean originales e íntegros. Requiere claves de consola válidas.',
        'Verify files': 'Verificar archivos',
        'Enable file verification: use': 'Activa la verificación de archivos: usa la verificación por',
        'verification to check origin, and': 'para comprobar el origen y por',
        'verification to check integrity.': 'para comprobar la integridad.',
        'Checks that the container decrypts and that every': 'Comprueba que el contenedor se descifra y que la firma de cada',
        'header signature is Nintendo\'s.': 'cabecera pertenece a Nintendo.',
        'Also hashes every byte of every': 'También calcula el hash de cada byte de cada',
        'and compares it against what the file claims, to ensure integrity.': 'y lo compara con el valor declarado por el archivo para comprobar su integridad.',
        'Windows compatible filenames': 'Nombres de archivo compatibles con Windows',
        'NS eShop Server enforces filename sanitization depending on the OS running it. Enabling this will sanitize filenames with Windows compatible characters and keep paths within the Windows length limit, this is needed when acessing libraries from Windows systems (e.g. SMB/NFS mount).': 'NS eShop Server adapta los nombres de archivo al sistema operativo. Esta opción usa caracteres compatibles con Windows y limita la longitud de las rutas; actívala si accedes a bibliotecas desde Windows (por ejemplo, mediante SMB o NFS).',
        'Library management': 'Gestión de biblioteca',
        'Library management settings': 'Ajustes de gestión de biblioteca',
        'Keep your library organized.': 'Mantén tu biblioteca organizada.',
        'Templates': 'Plantillas',
        'Available attributes for all templates:': 'Atributos disponibles en todas las plantillas:',
        'Available attributes for Base, Update, and DLC templates:': 'Atributos disponibles en las plantillas de juego base, actualización y DLC:',
        'The final computed paths will be relative to the root path of the library, the file extension is added automatically.': 'Las rutas finales serán relativas a la raíz de la biblioteca. La extensión se añade automáticamente.',
        'Make sure the templates contain': 'Asegúrate de que las plantillas incluyan',
        'for Tinfoil to recognize the apps.': 'para que Tinfoil reconozca las aplicaciones.',
        'Titles identification configuration.': 'Configuración de identificación de títulos.',
        'Missing console keys file.': 'Falta el archivo de claves de consola.',
        'Shop configuration and customization.': 'Configuración y personalización de la tienda.',
        'Configure your shop URL to enable host verification.': 'Configura la URL de la tienda para activar la verificación del host.',
        'Public shop': 'Tienda pública',
        'If enabled, Shop access from clients does not require authentication.': 'Si se activa, los clientes podrán acceder a la tienda sin autenticarse.',
        'Message of the day:': 'Mensaje del día:',
        'Clients': 'Clientes',
        'Enabled': 'Activado',
        'Encrypt shop': 'Cifrar tienda',
        'Scheduler': 'Programador',
        'Configure the periodic jobs. Interval format is number + unit (e.g., 2h, 30m, 1d), with units: s (seconds), m (minutes), h (hours), d (days). Set to 0 to disable.': 'Configura las tareas periódicas. El intervalo se expresa con un número y una unidad (por ejemplo, 2h, 30m, 1d): s (segundos), m (minutos), h (horas), d (días). Usa 0 para desactivarlo.',
        'Configure the periodic jobs. Interval format is': 'Configura las tareas periódicas. El formato del intervalo es',
        '(e.g.,': '(por ejemplo,',
        '), with units:': '), con las unidades:',
        '(seconds),': '(segundos),',
        '(minutes),': '(minutos),',
        '(hours),': '(horas),',
        '(days). Set to': '(días). Usa',
        'to disable.': 'para desactivarlo.',
        'TitleDB update interval:': 'Intervalo de actualización de TitleDB:',
        'Configure the number of task worker processes. More workers allow parallel processing of tasks (e.g., scanning, identifying files).': 'Configura la cantidad de procesos de trabajo. Más procesos permiten ejecutar tareas en paralelo (por ejemplo, analizar e identificar archivos).',
        'Worker count:': 'Cantidad de workers:',
        'Max concurrent I/O tasks:': 'Máximo de tareas de E/S simultáneas:',
        'Enable organizer': 'Activar organizador',
        'Enables automatic organization of identified files in the library, according to the templates below.': 'Organiza automáticamente los archivos identificados según las plantillas siguientes.',
        'Removes empty folders after organizing files.': 'Elimina las carpetas vacías después de organizar los archivos.',
        'Library-wide figures, counted at the moment the page loaded.': 'Datos de toda la biblioteca al cargar la página.',
        'Live view of the background work queue. Updates stream from the server as tasks progress.': 'Vista en directo de la cola de tareas. El servidor envía actualizaciones mientras se ejecutan.',
        'Delete user': 'Eliminar usuario',
        'Cancel': 'Cancelar',
        'Delete': 'Eliminar',
        'User': 'Usuario',
        'Permissions': 'Permisos',
        'Actions': 'Acciones',
        'Add new user': 'Añadir usuario',
        'Add a new user:': 'Añadir un usuario:',
        'Shop Access': 'Acceso a la tienda',
        'Backup Access': 'Acceso a copias',
        'Admin Access': 'Acceso de administrador',
        'Paths': 'Rutas',
        'Verification': 'Verificación',
        'Organizer': 'Organizador',
        'Titles': 'Títulos',
        'Library Region:': 'Región de la biblioteca:',
        'Library Language:': 'Idioma de la biblioteca:',
        'Region and Language used to get games informations.': 'Región e idioma usados para obtener la información de los juegos.',
        'Console Keys file:': 'Archivo de claves de la consola:',
        'Master key revisions:': 'Revisiones de master key:',
        'Shop': 'Tienda',
        'Shop URL:': 'URL de la tienda:',
        'Remove empty folders': 'Eliminar carpetas vacías',
        'Base template:': 'Plantilla de juego base:',
        'Update template:': 'Plantilla de actualización:',
        'DLC template:': 'Plantilla de DLC:',
        'Multi-content template:': 'Plantilla de contenido múltiple:',
        'Submit': 'Guardar',
        'Queue': 'En cola',
        'Nothing queued.': 'No hay tareas en cola.',
        'Showing the': 'Se muestran las',
        'oldest tasks — more are queued behind them.': 'tareas más antiguas; hay más en espera.',
        'Scheduled': 'Programadas',
        'Nothing scheduled.': 'No hay tareas programadas.',
        'Dismiss all failed tasks': 'Descartar todas las tareas fallidas',
        'No failures.': 'No hay tareas fallidas.',
        'Workers': 'Procesos de trabajo',
        'Worker': 'Proceso',
        'alive': 'activo',
        'Idle': 'En espera',
        'Update TitleDB': 'Actualizar TitleDB',
        'Process library files': 'Procesar archivos de biblioteca',
        'Update titles': 'Actualizar títulos',
        'Startup': 'Inicio',
        'Remove library': 'Eliminar biblioteca',
        'Refresh': 'Actualizar',
        'Extensions': 'Extensiones',
        'Extension': 'Extensión',
        'Files': 'Archivos',
        'Size': 'Tamaño',
        'Libraries': 'Bibliotecas',
        'Path': 'Ruta',
        'Verification status': 'Estado de verificación',
        'Status': 'Estado',
        'App types': 'Tipos de aplicación',
        'Type': 'Tipo',
        'Tracked': 'Registradas',
        'Nothing to report.': 'No hay datos que mostrar.',
        'identified': 'identificados',
        'Total size': 'Tamaño total',
        'across every library': 'en todas las bibliotecas',
        'Unidentified': 'Sin identificar',
        'files NS eShop Server could not match': 'archivos que NS eShop Server no pudo identificar',
        'Owned titles': 'Títulos disponibles',
        'in the catalogue': 'en el catálogo',
        'owned titles with every DLC': 'títulos con todos sus DLC',
        'owned titles on the latest update': 'títulos con la última actualización',
        'Owned apps': 'Aplicaciones disponibles',
        'of': 'de',
        'No valid console keys are loaded.': 'No hay claves de consola válidas cargadas.',
        'Signature only': 'Solo firma',
        'Full hash': 'Hash completo',
        'Finished': 'Finalizada',
        'finished': 'finalizada',
        'Cancelled': 'Cancelada',
        'cancelled': 'cancelada',
        'Failed': 'Fallidas',
        'failed': 'fallida',
        'due now': 'ahora',
        'running for': 'en ejecución desde hace',
        ' left': ' restantes',
        'Welcome, Anthony!': '¡Te damos la bienvenida, Anthony!',
        'Close': 'Cerrar',
        'Email': 'Correo electrónico',
    };

    const exact = new Map(Object.entries(spanish));
    const caseInsensitive = new Map(Object.entries(spanish).map(([english, translated]) => [english.toLowerCase(), translated]));
    const pluralLabels = {
        titles: 'títulos',
        complete: 'completos',
        'up to date': 'actualizados',
        files: 'archivos',
        images: 'imágenes',
    };
    const originalText = new WeakMap();
    const originalAttributes = new WeakMap();
    const ignored = 'script, style, noscript, code, pre, textarea, option, #gameGrid, .game-card, .game-icon';
    const originalTitle = document.title;
    let language = 'en';

    function translateValue(value) {
        if (language !== 'es') return value;

        const trimmed = value.trim();
        const normalized = trimmed.replace(/\s+/g, ' ');
        const translated = exact.get(normalized) || caseInsensitive.get(normalized.toLowerCase());
        if (translated) return value.replace(trimmed, translated);

        const catalogueCount = trimmed.match(/^([\d.,]+) catalogue entries?$/i);
        if (catalogueCount) {
            const noun = catalogueCount[1] === '1' ? 'elemento del catálogo' : 'elementos del catálogo';
            return value.replace(trimmed, `${catalogueCount[1]} ${noun}`);
        }

        const countLabel = trimmed.match(/^([\d.,]+) (titles|complete|up to date|files|images)$/i);
        if (countLabel) {
            const label = pluralLabels[countLabel[2].toLowerCase()] || countLabel[2];
            return value.replace(trimmed, `${countLabel[1]} ${label}`);
        }
        const ownedFraction = trimmed.match(/^([\d.,]+)\s*\/\s*([\d.,]+)\s+owned$/i);
        if (ownedFraction) return value.replace(trimmed, `${ownedFraction[1]}/${ownedFraction[2]} en tu biblioteca`);
        const identifiedCount = trimmed.match(/^([\d.,]+) identified$/i);
        if (identifiedCount) return value.replace(trimmed, `${identifiedCount[1]} identificados`);
        const workerName = trimmed.match(/^Worker (\d+)$/i);
        if (workerName) return value.replace(trimmed, `Proceso ${workerName[1]}`);
        const detailsLabel = trimmed.match(/^View details for (.+)$/i);
        if (detailsLabel) return value.replace(trimmed, `Ver detalles de ${detailsLabel[1]}`);
        const screenshotLabel = trimmed.match(/^Show screenshot (\d+)$/i);
        if (screenshotLabel) return value.replace(trimmed, `Mostrar captura ${screenshotLabel[1]}`);

        let result = value;
        result = result.replace(/^of ([\d.,]+) in the catalogue$/i, 'de $1 en el catálogo');
        result = result.replace(/\brunning for\b/gi, 'en ejecución desde hace');
        result = result.replace(/\bdue now\b/gi, 'ahora');
        result = result.replace(/\bfinished\b/gi, 'finalizada');
        result = result.replace(/\bcancelled\b/gi, 'cancelada');
        result = result.replace(/\bfailed\b/gi, 'fallida');
        result = result.replace(/ left\b/gi, ' restantes');
        result = result.replace(/\bin (?=\d)/gi, 'en ');
        return result;
    }

    function shouldIgnore(element) {
        return !element || element.closest(ignored);
    }

    function translateTextNode(node) {
        const element = node.parentElement;
        if (shouldIgnore(element)) return;

        const previous = originalText.get(node);
        const current = node.nodeValue;
        const source = previous && current === previous.translated ? previous.source : current;
        const translated = translateValue(source);
        originalText.set(node, {source, translated});
        if (current !== translated) node.nodeValue = translated;
    }

    function translateAttributes(element) {
        const attributes = ['aria-label', 'aria-valuetext', 'alt', 'placeholder', 'title', 'data-bs-title'];
        let saved = originalAttributes.get(element);
        if (!saved) {
            saved = {};
            originalAttributes.set(element, saved);
        }

        for (const name of attributes) {
            if (!element.hasAttribute(name)) continue;
            const current = element.getAttribute(name);
            const previous = saved[name];
            const source = previous && current === previous.translated ? previous.source : current;
            const translated = translateValue(source);
            saved[name] = {source, translated};
            if (current !== translated) element.setAttribute(name, translated);
        }
    }

    function translateTree(root) {
        if (root.nodeType === Node.TEXT_NODE) {
            translateTextNode(root);
            return;
        }
        if (root.nodeType === Node.ELEMENT_NODE) {
            if (shouldIgnore(root)) return;
            translateAttributes(root);
        }

        const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
        let node;
        while ((node = walker.nextNode())) translateTextNode(node);

        if (root.querySelectorAll) {
            root.querySelectorAll('*').forEach(element => {
                if (!shouldIgnore(element)) translateAttributes(element);
            });
        }
    }

    function setLanguage(value) {
        language = value === 'es' ? 'es' : 'en';
        document.documentElement.lang = language;
        try {
            localStorage.setItem('ownfoil-language', language);
        } catch (_) {
            // The selection still applies for this page if storage is unavailable.
        }
        document.querySelectorAll('#languageSelect').forEach(select => {
            select.value = language;
        });
        translateTree(document.body);
        const pageTitle = originalTitle.startsWith('NS eShop Server | ')
            ? translateValue(originalTitle.slice('NS eShop Server | '.length))
            : translateValue(originalTitle);
        document.title = originalTitle.startsWith('NS eShop Server | ') ? `NS eShop Server | ${pageTitle}` : pageTitle;
    }

    function t(value) {
        return translateValue(value);
    }

    window.ownfoilI18n = {t, get language() { return language; }};

    let savedLanguage = '';
    try {
        savedLanguage = localStorage.getItem('ownfoil-language') || '';
    } catch (_) {
        // Fall back to the browser's language when storage is unavailable.
    }
    const initialLanguage = savedLanguage || (navigator.language.toLowerCase().startsWith('es') ? 'es' : 'en');
    document.querySelectorAll('#languageSelect').forEach(select => {
        select.addEventListener('change', () => setLanguage(select.value));
    });
    setLanguage(initialLanguage);

    new MutationObserver(records => {
        for (const record of records) {
            record.addedNodes.forEach(node => {
                if (node.nodeType === Node.ELEMENT_NODE || node.nodeType === Node.TEXT_NODE) translateTree(node);
            });
            if (record.type === 'characterData') translateTextNode(record.target);
        }
    }).observe(document.body, {childList: true, characterData: true, subtree: true});
})();