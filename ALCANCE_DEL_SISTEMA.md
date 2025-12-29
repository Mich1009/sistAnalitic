# 📋 ALCANCE DEL SISTEMA SADES

## 🎯 Descripción General

**SADES** es un **Sistema de Gestión Académica** web desarrollado con Flask que permite a instituciones educativas gestionar integralmente el seguimiento de estudiantes, cursos, calificaciones y detectar riesgos académicos.

## 👥 Usuarios del Sistema

El sistema está diseñado para 3 tipos de usuarios:

### 1. **Administrador**
- Acceso completo a todo el sistema
- Gestión de usuarios
- Configuración del sistema
- Visualización de todos los reportes
- **Usuario:** admin | **Contraseña:** admin123

### 2. **Coordinador Académico**
- Gestión de estudiantes
- Gestión de cursos
- Visualización de reportes
- Seguimiento de riesgo académico
- **Usuario:** coordinador | **Contraseña:** coord123

### 3. **Docente**
- Registro de calificaciones
- Registro de asistencias
- Visualización de sus cursos
- Generación de reportes de sus estudiantes
- **Usuario:** docente | **Contraseña:** docente123

## 📊 Módulos Principales

### 1. **Autenticación (Auth)**
- Login seguro con roles
- Control de acceso basado en roles (RBAC)
- Gestión de sesiones
- Recuperación de contraseña

### 2. **Dashboard**
- Panel principal con estadísticas
- Resumen de estudiantes
- Resumen de cursos
- Indicadores de riesgo académico
- Gráficos y visualizaciones

### 3. **Gestión de Estudiantes**
- Crear, editar, eliminar estudiantes
- Visualizar información de estudiantes
- Historial académico
- Contacto y datos personales
- Estado activo/inactivo

### 4. **Gestión de Cursos**
- Crear, editar, eliminar cursos
- Organizar cursos por ciclos académicos
- Asignar créditos
- Definir semestres
- Gestionar docentes por curso

### 5. **Inscripciones**
- Inscribir estudiantes en cursos
- Visualizar inscripciones
- Cambiar estado de inscripción
- Historial de inscripciones

### 6. **Evaluaciones**
- Crear evaluaciones (parciales, exámenes)
- Definir peso de evaluaciones
- Gestionar tipos de evaluación
- Organizar por curso

### 7. **Registro de Calificaciones**
- Ingresar notas de estudiantes
- Editar calificaciones
- Visualizar promedio por curso
- Historial de calificaciones
- Cálculo automático de promedios

### 8. **Control de Asistencia**
- Registrar asistencia diaria
- Marcar presente/ausente
- Justificar inasistencias
- Visualizar porcentaje de asistencia
- Reportes de asistencia

### 9. **Seguimiento de Riesgo Académico**
- Cálculo automático de riesgo
- Categorización: Sin Riesgo, Alerta Amarilla, Alerta Roja
- Análisis de factores de riesgo:
  - Rendimiento académico
  - Asistencia
  - Distribución de riesgo por curso
- Historial de evaluaciones de riesgo
- Alertas automáticas

### 10. **Intervenciones Académicas**
- Registrar intervenciones
- Tipos: Tutoría, Consejería, Seguimiento
- Descripción de intervención
- Responsable de la intervención
- Estado: Pendiente, En Proceso, Completada
- Resultados y observaciones

### 11. **Generación de Reportes**
- **Reportes Individuales:**
  - Reporte de riesgo por estudiante
  - Información académica completa
  - Historial de calificaciones
  - Asistencia
  - Evaluación de riesgo
  
- **Reportes Generales:**
  - Reporte de riesgo por semestre
  - Estadísticas de estudiantes en riesgo
  - Distribución por categoría
  - Listado de estudiantes por categoría
  
- **Formatos:**
  - HTML (visualización en navegador)
  - PDF (descarga e impresión)
  
- **Características:**
  - Generación automática
  - Historial de reportes
  - Descarga de reportes anteriores
  - Regeneración automática si falta archivo

### 12. **Importación de Datos**
- Importar estudiantes desde Excel
- Importar cursos desde Excel
- Importar calificaciones desde Excel
- Validación de datos
- Reporte de errores

### 13. **Administración**
- Gestión de usuarios
- Configuración del sistema
- Gestión de ciclos académicos
- Auditoría de cambios
- Respaldos de base de datos

## 🔄 Flujos de Trabajo

### Flujo 1: Inscripción de Estudiantes
```
1. Crear estudiante
2. Crear curso
3. Inscribir estudiante en curso
4. Sistema registra fecha de inscripción
```

### Flujo 2: Registro de Calificaciones
```
1. Docente crea evaluaciones
2. Docente ingresa notas
3. Sistema calcula promedio
4. Sistema evalúa riesgo
5. Genera alertas si es necesario
```

### Flujo 3: Seguimiento de Riesgo
```
1. Sistema calcula riesgo automáticamente
2. Categoriza estudiantes
3. Genera alertas
4. Coordinador revisa alertas
5. Coordinador registra intervención
6. Genera reporte de seguimiento
```

### Flujo 4: Generación de Reportes
```
1. Usuario selecciona tipo de reporte
2. Selecciona parámetros (estudiante, semestre, etc.)
3. Selecciona formato (HTML o PDF)
4. Sistema genera reporte
5. Usuario descarga o visualiza
6. Sistema guarda en historial
```

## 📈 Funcionalidades Clave

### Cálculo de Riesgo Académico
El sistema calcula automáticamente el riesgo basado en:

- **Rendimiento (50%):** Promedio de calificaciones
- **Asistencia (30%):** Porcentaje de asistencia
- **Distribución (20%):** Cantidad de cursos con bajo rendimiento

**Categorías:**
- 🟢 **Sin Riesgo:** Puntaje < 0.5
- 🟡 **Alerta Amarilla:** Puntaje 0.5 - 0.7
- 🔴 **Alerta Roja:** Puntaje > 0.7

### Alertas Automáticas
- Notificación cuando estudiante entra en riesgo
- Notificación cuando mejora su situación
- Recordatorios de intervención pendiente

### Historial Completo
- Registro de todos los cambios
- Auditoría de quién hizo qué y cuándo
- Trazabilidad de decisiones

## 💾 Base de Datos

### Tablas Principales
- **usuarios** - Usuarios del sistema
- **estudiantes** - Información de estudiantes
- **cursos** - Catálogo de cursos
- **ciclos** - Ciclos académicos
- **inscripciones** - Inscripciones estudiante-curso
- **evaluaciones** - Evaluaciones por curso
- **notas** - Calificaciones de estudiantes
- **asistencias** - Registro de asistencia
- **seguimiento_riesgo** - Evaluaciones de riesgo
- **intervenciones** - Intervenciones académicas
- **reportes** - Historial de reportes generados

### Datos Incluidos
- 20 estudiantes de prueba
- 46 cursos
- 8 ciclos académicos
- 40 inscripciones
- 160 notas
- 800 registros de asistencia
- 20 evaluaciones de riesgo
- 5 intervenciones

## 🎨 Interfaz de Usuario

### Características de UI
- Diseño responsivo (funciona en desktop, tablet, móvil)
- Interfaz intuitiva y fácil de usar
- Menú de navegación principal
- Breadcrumbs para orientación
- Tablas con paginación
- Formularios validados
- Mensajes de confirmación
- Alertas de error

### Paleta de Colores
- Primario: #4FB7B3 (Turquesa)
- Secundario: #637AB9 (Azul)
- Oscuro: #31326F (Azul oscuro)
- Claro: #A8FBD3 (Verde claro)

## 🔒 Seguridad

### Características de Seguridad
- Autenticación con contraseña hasheada
- Control de acceso basado en roles
- Protección CSRF
- Validación de entrada
- Sanitización de datos
- Sesiones seguras
- Encriptación de datos sensibles

## 📱 Compatibilidad

### Navegadores Soportados
- Chrome/Chromium
- Firefox
- Safari
- Edge

### Sistemas Operativos
- Windows
- macOS
- Linux

### Requisitos Técnicos
- Python 3.8+
- PostgreSQL 12+
- 100MB de espacio en disco
- Conexión a internet (para CDN de Bootstrap)

## 🚀 Capacidades de Escalabilidad

El sistema puede manejar:
- Hasta 10,000 estudiantes
- Hasta 500 cursos
- Hasta 100,000 registros de asistencia
- Generación de reportes en tiempo real

## 📊 Reportes Disponibles

### Reportes Individuales
- Reporte de riesgo académico por estudiante
- Historial académico completo
- Evaluación de factores de riesgo
- Recomendaciones personalizadas

### Reportes Generales
- Reporte de riesgo por semestre
- Estadísticas de estudiantes en riesgo
- Distribución por categoría de riesgo
- Análisis de tendencias

### Exportación
- PDF con formato profesional
- HTML para visualización web
- Historial de reportes generados

## 🔧 Mantenimiento

### Tareas de Mantenimiento
- Backup automático de base de datos
- Limpieza de archivos temporales
- Actualización de datos de riesgo
- Monitoreo de rendimiento

### Monitoreo
- Logs de actividad
- Auditoría de cambios
- Alertas de errores
- Estadísticas de uso

## 📈 Métricas y KPIs

El sistema proporciona:
- Número de estudiantes en riesgo
- Porcentaje de asistencia promedio
- Promedio de calificaciones
- Tendencias de riesgo académico
- Efectividad de intervenciones

## 🎓 Casos de Uso

### Caso 1: Identificar Estudiantes en Riesgo
```
1. Coordinador accede al dashboard
2. Ve estudiantes en alerta roja
3. Genera reporte individual
4. Revisa factores de riesgo
5. Registra intervención
```

### Caso 2: Seguimiento de Intervención
```
1. Docente registra calificaciones
2. Sistema calcula riesgo
3. Genera alerta si hay cambio
4. Coordinador revisa intervención
5. Actualiza estado de intervención
```

### Caso 3: Análisis de Semestre
```
1. Coordinador genera reporte general
2. Analiza distribución de riesgo
3. Identifica patrones
4. Toma decisiones académicas
5. Exporta reporte en PDF
```

## 🎯 Objetivos del Sistema

1. **Prevención:** Identificar estudiantes en riesgo tempranamente
2. **Intervención:** Facilitar intervenciones académicas oportunas
3. **Seguimiento:** Monitorear progreso de estudiantes
4. **Análisis:** Proporcionar datos para toma de decisiones
5. **Mejora:** Aumentar tasa de retención y éxito académico

## 📞 Soporte y Documentación

- README.md - Guía de instalación
- INSTALAR_WKHTMLTOPDF.md - Instalación de dependencias
- SOLUCION_DESCARGA_PDF.md - Solución de problemas
- ESTADO_SISTEMA.md - Estado del sistema

## ✨ Ventajas del Sistema

✅ Automatización de cálculos de riesgo
✅ Alertas tempranas de problemas académicos
✅ Generación de reportes profesionales
✅ Interfaz intuitiva y fácil de usar
✅ Datos centralizados y seguros
✅ Acceso basado en roles
✅ Historial completo de cambios
✅ Escalable y mantenible
✅ Código limpio y documentado
✅ Listo para producción

---

**SADES** es una solución completa para la gestión académica y seguimiento de riesgo estudiantil.
