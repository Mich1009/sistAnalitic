# Sistema de Gestión Académica - SADES

Sistema web desarrollado con Flask para la gestión integral de estudiantes, cursos, calificaciones y seguimiento de riesgo académico.

## 🎯 Características Principales

- ✅ Autenticación y control de acceso por roles
- ✅ Gestión de estudiantes y cursos
- ✅ Registro de calificaciones y asistencias
- ✅ Sistema de seguimiento de riesgo académico
- ✅ Generación de reportes en PDF
- ✅ Importación de datos desde Excel
- ✅ Panel de administración
- ✅ Base de datos con 20 estudiantes y 46 cursos de prueba

## 📋 Requisitos Previos

- **Python 3.8 o superior**
- **PostgreSQL 12 o superior** - [Descargar](https://www.postgresql.org/download/)
- **pip** (gestor de paquetes de Python)

## 🚀 Instalación Rápida (5 pasos)

### 1. Crear Entorno Virtual

**Windows (cmd):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Importar Base de Datos

```bash
python import_db.py
```

El script hará automáticamente:
- ✅ Verificar que PostgreSQL esté corriendo
- ✅ Crear la base de datos `sades_db`
- ✅ Importar todos los datos (20 estudiantes, 46 cursos, etc.)
- ✅ Verificar que la importación fue exitosa

### 4. Ejecutar la Aplicación

```bash
python run.py
```

Deberías ver:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 5. Acceder a la Aplicación

Abre tu navegador y ve a:
```
http://localhost:5000
```

## 🔐 Usuarios de Prueba

| Rol | Usuario | Contraseña | Email |
|-----|---------|-----------|-------|
| Administrador | admin | admin123 | admin@sades.edu |
| Coordinador | coordinador | coord123 | coordinador@sades.edu |
| Docente | docente | docente123 | docente@sades.edu |

## 📊 Datos Incluidos

Después de importar la base de datos, tendrás:

- **20 estudiantes** con información completa
- **46 cursos** organizados en 8 ciclos académicos
- **40 inscripciones** de estudiantes en cursos
- **8 evaluaciones** (parciales y exámenes)
- **160 notas** de estudiantes
- **800 registros de asistencia**
- **20 evaluaciones de riesgo** académico
- **5 intervenciones** académicas
- **3 usuarios** (admin, coordinador, docente)

## 📁 Estructura del Proyecto

```
app/
├── modules/              # Módulos funcionales
│   ├── auth/            # Autenticación
│   ├── dashboard/       # Panel principal
│   ├── estudiantes/     # Gestión de estudiantes
│   ├── cursos/          # Gestión de cursos
│   ├── evaluaciones/    # Calificaciones
│   ├── asistencias/     # Control de asistencia
│   ├── seguimiento/     # Seguimiento de riesgo
│   ├── reportes/        # Generación de reportes
│   ├── importacion/     # Importación de datos
│   ├── inscripciones/   # Inscripciones
│   └── admin/           # Administración
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Plantillas HTML
├── models.py            # Modelos de base de datos
├── extensions.py        # Extensiones Flask
└── __init__.py          # Inicialización de la app

config.py               # Configuración de la aplicación
run.py                  # Punto de entrada
requirements.txt        # Dependencias del proyecto
import_db.py            # Script de importación de BD
grupo1_postgres.sql     # Base de datos PostgreSQL
.env                    # Variables de entorno
```

## ⚙️ Configuración

### Variables de Entorno (.env)

El archivo `.env` ya está configurado para PostgreSQL:

```env
# Configuración Flask
FLASK_CONFIG=development
SECRET_KEY=sades_secret_key_2025_development

# Base de Datos - Desarrollo (PostgreSQL)
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sades_db

# Base de Datos - Producción (opcional)
PROD_SECRET_KEY=sades_secret_key_2025_production
PROD_DB_USER=postgres_prod
PROD_DB_PASSWORD=prod_password_secure
PROD_DB_HOST=prod_server.com
PROD_DB_PORT=5432
PROD_DB_NAME=sades_db_prod
```

**Nota:** Si tu contraseña de PostgreSQL es diferente, actualiza `DB_PASSWORD` en el archivo `.env`.

### Configuración de la Aplicación (config.py)

La aplicación está configurada para usar PostgreSQL:

```python
# Desarrollo
SQLALCHEMY_DATABASE_URI = postgresql://usuario:contraseña@localhost:5432/sades_db

# Producción
SQLALCHEMY_DATABASE_URI = postgresql://usuario:contraseña@servidor:5432/sades_db_prod
```

## 🎨 Paleta de Colores

- **Primario:** #4FB7B3
- **Secundario:** #637AB9
- **Oscuro:** #31326F
- **Claro:** #A8FBD3

## 🔧 Solución de Problemas

### Error: "psql: command not found"
PostgreSQL no está en el PATH. Reinstálalo y marca la opción "Add PostgreSQL to PATH".

### Error: "could not connect to server"
- Verifica que PostgreSQL esté corriendo
- Verifica las credenciales en `.env`
- Asegúrate de que el puerto 5432 esté disponible

### Error: "database does not exist"
Ejecuta el script de importación:
```bash
python import_db.py
```

### Error: "ModuleNotFoundError: No module named 'psycopg2'"
Instala el driver de PostgreSQL:
```bash
pip install psycopg2-binary
```

### Error: "FATAL: Ident authentication failed"
Verifica la contraseña en `.env` o resetéala en PostgreSQL.

### La aplicación no inicia
- Verifica que el entorno virtual esté activado
- Verifica que todas las dependencias estén instaladas
- Verifica que PostgreSQL esté corriendo

## 📚 Documentación Adicional

- [Pasos de Puesta en Marcha](PASOS_PUESTA_EN_MARCHA.md) - Guía completa paso a paso
- [Configuración de PostgreSQL](POSTGRES_SETUP.md) - Detalles técnicos de PostgreSQL
- [Guía de Importación](IMPORT_DB_README.md) - Información sobre el script de importación

## 🚀 Próximos Pasos (Después de puesta en marcha)

1. Explorar el dashboard con usuario admin
2. Crear nuevos estudiantes
3. Registrar cursos adicionales
4. Cargar calificaciones
5. Generar reportes
6. Configurar intervenciones académicas

## 💡 Tips Útiles

- Mantén PostgreSQL corriendo mientras usas la app
- Guarda regularmente tus cambios
- Haz backups de la base de datos
- Usa el usuario admin para configuración inicial
- Crea usuarios adicionales según sea necesario

## 🐛 Reportar Problemas

Si encuentras algún problema:

1. Verifica la sección "Solución de Problemas"
2. Revisa los logs de la aplicación
3. Consulta la documentación adicional
4. Verifica que PostgreSQL esté corriendo

## 📝 Notas Importantes

- La aplicación usa PostgreSQL en lugar de MySQL
- Los datos de prueba incluyen información realista para testing
- El script de importación es seguro y no sobrescribe datos sin preguntar
- Puedes ejecutar el script de importación múltiples veces sin problemas
- Asegúrate de hacer backup de la base de datos regularmente

## ✨ ¡Listo para usar!

Sigue los 5 pasos de instalación rápida y tu aplicación SADES estará lista para usar.

**¡Bienvenido a SADES - Sistema de Seguimiento Estudiantil!** 🎉

## Usuarios de Prueba

| Rol | Usuario | Contraseña | Email | Permisos |
|-----|---------|-----------|-------|----------|
| Administrador | admin | admin123 | admin@sades.edu | Acceso completo a todo el sistema |
| Coordinador | coordinador | coord123 | coordinador@sades.edu | Gestión de estudiantes y cursos |
| Docente | docente | docente123 | docente@sades.edu | Registro de notas y asistencias |

## Estructura del Proyecto

```
app/
├── modules/          # Módulos funcionales
│   ├── auth/        # Autenticación
│   ├── dashboard/   # Panel principal
│   ├── estudiantes/ # Gestión de estudiantes
│   ├── cursos/      # Gestión de cursos
│   ├── evaluaciones/# Calificaciones
│   ├── asistencias/ # Control de asistencia
│   ├── seguimiento/ # Seguimiento de riesgo
│   ├── reportes/    # Generación de reportes
│   └── admin/       # Administración
├── static/          # Archivos estáticos (CSS, JS, imágenes)
├── templates/       # Plantillas HTML
├── models.py        # Modelos de base de datos
├── extensions.py    # Extensiones Flask
└── __init__.py      # Inicialización de la app

config.py            # Configuración de la aplicación
run.py              # Punto de entrada
requirements.txt    # Dependencias del proyecto
```

## Características Principales

- ✅ Autenticación y control de acceso por roles
- ✅ Gestión de estudiantes y cursos
- ✅ Registro de calificaciones y asistencias
- ✅ Sistema de seguimiento de riesgo académico
- ✅ Generación de reportes en PDF
- ✅ Importación de datos desde Excel
- ✅ Panel de administración

## Paleta de Colores

- Primario: #4FB7B3
- Secundario: #637AB9
- Oscuro: #31326F
- Claro: #A8FBD3

## Solución de Problemas

### Error: "No module named 'app'"
- Asegúrate de estar en la raíz del proyecto
- Verifica que el entorno virtual esté activado

### Error de conexión a base de datos
- Verifica que MySQL esté corriendo
- Comprueba las credenciales en el archivo `.env`
- Asegúrate de que la base de datos existe

### Error: "ModuleNotFoundError"
- Ejecuta: `pip install -r requirements.txt`
- Verifica que el entorno virtual esté activado

## Notas Importantes

- Nunca commits el archivo `.env` con credenciales reales
- Usa `FLASK_CONFIG=development` para desarrollo
- Para producción, configura `FLASK_CONFIG=production`
- Asegúrate de tener wkhtmltopdf instalado para generar PDFs
