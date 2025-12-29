# 📚 Documentación de API - SADES

## Versión: 1.0.0

---

## 🔐 Autenticación

Todas las rutas requieren autenticación. Usa las credenciales de usuario para acceder.

```
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=usuario&password=contraseña
```

---

## 📊 Endpoints de Búsqueda

### Búsqueda Global
```
GET /busqueda/global?q=término
```

**Parámetros:**
- `q` (string): Término de búsqueda

**Respuesta:**
```json
{
  "estudiantes": [...],
  "cursos": [...],
  "reportes": [...],
  "total": 5
}
```

### API Búsqueda Global (Autocomplete)
```
GET /busqueda/api/global?q=término
```

**Respuesta:**
```json
{
  "estudiantes": [
    {
      "id": 1,
      "texto": "77415003 - Juan García",
      "tipo": "estudiante",
      "enlace": "/estudiantes/detalle/1"
    }
  ],
  "cursos": [...],
  "reportes": [...]
}
```

---

## 👥 Endpoints de Estudiantes

### Listar Estudiantes
```
GET /estudiantes/?page=1&search=término
```

**Parámetros:**
- `page` (int): Número de página
- `search` (string): Término de búsqueda

**Respuesta:** HTML con lista paginada

### Detalle de Estudiante
```
GET /estudiantes/<id>
```

**Parámetros:**
- `id` (int): ID del estudiante

**Respuesta:** HTML con detalles

### Crear Estudiante
```
POST /estudiantes/crear
Content-Type: application/x-www-form-urlencoded

codigo_estudiante=77415003&nombres=Juan&apellidos=García&email=juan@example.com
```

### Editar Estudiante
```
POST /estudiantes/<id>/editar
Content-Type: application/x-www-form-urlencoded

codigo_estudiante=77415003&nombres=Juan&apellidos=García&email=juan@example.com
```

### Eliminar Estudiante
```
POST /estudiantes/<id>/eliminar
```

### Exportar a Excel
```
GET /estudiantes/exportar/excel
```

**Respuesta:** Archivo XLSX

### Exportar a CSV
```
GET /estudiantes/exportar/csv
```

**Respuesta:** Archivo CSV

---

## 📋 Endpoints de Reportes

### Generar Reporte Individual
```
POST /reportes/individual
Content-Type: application/x-www-form-urlencoded

estudiante_id=1&formato=pdf
```

**Parámetros:**
- `estudiante_id` (int): ID del estudiante
- `formato` (string): 'pdf' o 'html'

**Respuesta:** PDF o HTML

### Generar Reporte General
```
POST /reportes/general
Content-Type: application/x-www-form-urlencoded

semestre=2025-1&formato=pdf
```

**Parámetros:**
- `semestre` (string): Semestre (ej: 2025-1)
- `formato` (string): 'pdf' o 'html'

**Respuesta:** PDF o HTML

### Historial de Reportes
```
GET /reportes/historial?page=1
```

**Parámetros:**
- `page` (int): Número de página

**Respuesta:** HTML con historial

---

## ⚠️ Endpoints de Seguimiento

### Calcular Riesgo
```
POST /seguimiento/calcular
Content-Type: application/x-www-form-urlencoded

semestre=2025-1
```

**Parámetros:**
- `semestre` (string): Semestre a evaluar

**Respuesta:** Redirect a resultados

### Ver Resultados
```
GET /seguimiento/resultados?page=1
```

**Parámetros:**
- `page` (int): Número de página

**Respuesta:** HTML con resultados

---

## 📚 Endpoints de Cursos

### Listar Cursos
```
GET /cursos/?page=1
```

**Parámetros:**
- `page` (int): Número de página

**Respuesta:** HTML con lista

### Detalle de Curso
```
GET /cursos/<id>
```

**Parámetros:**
- `id` (int): ID del curso

**Respuesta:** HTML con detalles

---

## 📝 Códigos de Estado HTTP

| Código | Significado |
|--------|-------------|
| 200 | OK - Solicitud exitosa |
| 302 | Redirect - Redirección |
| 400 | Bad Request - Solicitud inválida |
| 401 | Unauthorized - No autenticado |
| 403 | Forbidden - No autorizado |
| 404 | Not Found - Recurso no encontrado |
| 500 | Internal Server Error - Error del servidor |

---

## 🔄 Flujos Comunes

### Flujo: Buscar y Ver Detalles de Estudiante
```
1. GET /busqueda/global?q=Juan
2. GET /estudiantes/detalle/1
```

### Flujo: Exportar Estudiantes
```
1. GET /estudiantes/exportar/excel
   (Descarga archivo XLSX)
```

### Flujo: Generar Reporte
```
1. POST /reportes/individual
   (Genera reporte)
2. GET /reportes/historial
   (Ve historial)
```

---

## 📊 Formatos de Respuesta

### Estudiante
```json
{
  "id": 1,
  "codigo_estudiante": "77415003",
  "nombres": "Juan",
  "apellidos": "García",
  "email": "juan@example.com",
  "telefono": "+34 123 456 789",
  "fecha_inscripcion": "2025-01-15",
  "activo": true
}
```

### Curso
```json
{
  "id": 1,
  "codigo_curso": "MAT101",
  "nombre_curso": "Matemáticas I",
  "creditos": 3,
  "semestre": "2025-1",
  "activo": true
}
```

### Seguimiento de Riesgo
```json
{
  "id": 1,
  "estudiante_id": 1,
  "semestre": "2025-1",
  "categoria_riesgo": "ALERTA_ROJA",
  "puntaje_riesgo": 0.81,
  "fecha_evaluacion": "2025-12-26",
  "factores_riesgo": {
    "asistencia": 72.5,
    "promedio_calificaciones": 8.9,
    "materias_reprobadas": 2
  }
}
```

---

## 🚀 Ejemplos de Uso

### Ejemplo 1: Buscar estudiante
```bash
curl -X GET "http://localhost:5000/busqueda/global?q=Juan" \
  -H "Cookie: session=..."
```

### Ejemplo 2: Exportar a Excel
```bash
curl -X GET "http://localhost:5000/estudiantes/exportar/excel" \
  -H "Cookie: session=..." \
  -o estudiantes.xlsx
```

### Ejemplo 3: Generar reporte
```bash
curl -X POST "http://localhost:5000/reportes/individual" \
  -H "Cookie: session=..." \
  -d "estudiante_id=1&formato=pdf" \
  -o reporte.pdf
```

---

## 📝 Notas

- Todas las rutas requieren autenticación
- Los formatos de fecha son DD/MM/YYYY
- Los IDs son números enteros
- Las respuestas HTML incluyen CSRF tokens

---

**Última actualización:** 28 de Diciembre de 2025
