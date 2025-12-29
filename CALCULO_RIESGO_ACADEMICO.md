# 📊 CÁLCULO DE RIESGO ACADÉMICO EN SADES

## 🎯 ¿Cómo se Calcula el Riesgo?

El sistema calcula automáticamente el riesgo académico de cada estudiante basándose en **3 factores principales**:

## 📈 Los 3 Factores de Riesgo

### 1. 📚 RENDIMIENTO ACADÉMICO (Peso: 50%)

**¿Qué mide?**
- Promedio de calificaciones del estudiante en el semestre actual
- Cantidad de evaluaciones completadas
- Completitud de evaluaciones

**¿Cómo se calcula?**
```
Promedio = Suma de todas las notas / Cantidad de evaluaciones

Escala de Riesgo:
- Promedio ≥ 14 → Valor: 0.1 (Bajo riesgo)
- Promedio 12-14 → Valor: 0.3 (Riesgo moderado)
- Promedio 10-12 → Valor: 0.6 (Riesgo alto)
- Promedio < 10 → Valor: 0.9 (Riesgo crítico)
```

**Ejemplo:**
```
Estudiante: Juan García
Cursos inscritos: 2
- Curso 1: Promedio 8.9 (4 evaluaciones)
- Curso 2: Promedio 9.3 (4 evaluaciones)

Promedio General: (8.9 + 9.3) / 2 = 9.1
Valor de Riesgo: 0.9 (Crítico)
```

**Ajuste por Completitud:**
- Si tiene < 30% de evaluaciones esperadas → Reduce riesgo 40%
- Si tiene 30-60% de evaluaciones → Reduce riesgo 20%
- Si tiene > 60% de evaluaciones → Sin ajuste

### 2. 📅 ASISTENCIA (Peso: 30%)

**¿Qué mide?**
- Porcentaje de clases asistidas en el semestre
- Inasistencias justificadas vs injustificadas
- Consistencia de asistencia

**¿Cómo se calcula?**
```
Porcentaje Asistencia = (Clases Asistidas / Total de Clases) × 100

Escala de Riesgo:
- Asistencia ≥ 85% → Valor: 0.1 (Bajo riesgo)
- Asistencia 75-85% → Valor: 0.3 (Riesgo moderado)
- Asistencia 65-75% → Valor: 0.6 (Riesgo alto)
- Asistencia < 65% → Valor: 0.9 (Riesgo crítico)
```

**Ejemplo:**
```
Estudiante: María López
Total de clases: 40
Clases asistidas: 29
Clases justificadas: 2

Porcentaje: (29 / 40) × 100 = 72.5%
Valor de Riesgo: 0.6 (Alto)
```

### 3. 🎯 DISTRIBUCIÓN DE RIESGO (Peso: 20%)

**¿Qué mide?**
- Cantidad de cursos donde el estudiante tiene bajo rendimiento
- Concentración del riesgo en pocos cursos vs distribuido

**¿Cómo se calcula?**
```
Cursos en Riesgo = Cursos con promedio < 12

Proporción = Cursos en Riesgo / Total de Cursos

Escala de Riesgo:
- 0% cursos en riesgo → Valor: 0.1
- 1-30% cursos en riesgo → Valor: 0.3
- 31-60% cursos en riesgo → Valor: 0.6
- > 60% cursos en riesgo → Valor: 0.9
```

**Ejemplo:**
```
Estudiante: Carlos Pérez
Cursos inscritos: 4
- Curso 1: Promedio 15.2 ✅
- Curso 2: Promedio 14.1 ✅
- Curso 3: Promedio 9.8 ❌
- Curso 4: Promedio 11.5 ❌

Cursos en riesgo: 2 de 4 = 50%
Valor de Riesgo: 0.6 (Alto)
```

## 🧮 Fórmula Final de Riesgo

```
PUNTAJE TOTAL = (Rendimiento × 0.5) + (Asistencia × 0.3) + (Distribución × 0.2)

Rango: 0.0 a 1.0
```

## 🚨 Categorías de Riesgo

### 🟢 SIN RIESGO
```
Puntaje: 0.0 - 0.4
Significado: Estudiante con buen desempeño
Acciones: Mantener seguimiento regular
```

### 🟡 ALERTA AMARILLA
```
Puntaje: 0.4 - 0.7
Significado: Estudiante con problemas académicos moderados
Acciones: 
- Seguimiento quincenal
- Tutoría académica
- Establecer metas de mejora
```

### 🔴 ALERTA ROJA
```
Puntaje: 0.7 - 1.0
Significado: Estudiante en riesgo crítico
Acciones:
- Intervención inmediata
- Reunión urgente
- Notificar a familia
- Evaluar ajuste de matrícula
```

## 📊 Ejemplo Completo de Cálculo

### Caso: Juan García

**Datos del Estudiante:**
```
Semestre: 2025-1
Cursos inscritos: 2
- Diseño Gráfico
- Programación Python
```

**Factor 1: Rendimiento Académico**
```
Diseño Gráfico:
- PC1: 7.44
- PC2: 12.03
- EX1: 10.03
- EX2: 7.06
Promedio: 9.14

Programación Python:
- PC1: 9.07
- PC2: 9.68
- EX1: 6.23
- EX2: 9.48
Promedio: 8.62

Promedio General: (9.14 + 8.62) / 2 = 8.88
Valor: 0.9 (Crítico)
Descripción: "Promedio: 8.9 | 8 evaluaciones | Completitud: 100%"
```

**Factor 2: Asistencia**
```
Total de clases: 40
Clases asistidas: 29
Clases justificadas: 0

Porcentaje: (29 / 40) × 100 = 72.5%
Valor: 0.6 (Alto)
Descripción: "Asistencia: 72.5% (29/40 clases)"
```

**Factor 3: Distribución de Riesgo**
```
Cursos inscritos: 2
Cursos con promedio < 12: 2

Proporción: 2/2 = 100%
Valor: 0.9 (Crítico)
Descripción: "2.0 de 2 cursos requieren atención"
```

**Cálculo Final:**
```
Puntaje = (0.9 × 0.5) + (0.6 × 0.3) + (0.9 × 0.2)
Puntaje = 0.45 + 0.18 + 0.18
Puntaje = 0.81

Categoría: 🔴 ALERTA ROJA (Puntaje > 0.7)
```

**Recomendaciones Generadas:**
```
🚨 INTERVENCIÓN INMEDIATA - Reunión urgente requerida
📚 Reforzamiento académico inmediato
⏰ Revisar técnicas de estudio y planificación
📅 Plan de mejora de asistencia con seguimiento semanal
🏫 Coordinar con bienestar estudiantil
🎯 Priorizar atención en cursos críticos
📊 Evaluar carga académica con coordinación
📞 Notificar a departamento estudiantil y familia
⚖️ Evaluar posible ajuste de matrícula
```

## 📈 Visualización del Riesgo

```
BAJO RIESGO (0.0 - 0.4)
████░░░░░░░░░░░░░░░░ 20%
🟢 Sin Riesgo

RIESGO MODERADO (0.4 - 0.7)
████████████░░░░░░░░ 60%
🟡 Alerta Amarilla

RIESGO CRÍTICO (0.7 - 1.0)
████████████████████ 100%
🔴 Alerta Roja
```

## 🔄 Cuándo se Calcula el Riesgo

El riesgo se calcula automáticamente:

1. **Al registrar una calificación** - Se recalcula inmediatamente
2. **Al registrar asistencia** - Se recalcula inmediatamente
3. **Diariamente** - Actualización automática cada día
4. **Bajo demanda** - Cuando el coordinador lo solicita

## 📊 Datos que Afectan el Riesgo

### Aumentan el Riesgo ⬆️
- Calificaciones bajas (< 10)
- Inasistencias frecuentes
- Bajo rendimiento en múltiples cursos
- Pocas evaluaciones completadas

### Disminuyen el Riesgo ⬇️
- Calificaciones altas (> 14)
- Asistencia consistente (> 85%)
- Buen rendimiento en todos los cursos
- Evaluaciones completadas

## 🎯 Casos de Uso

### Caso 1: Estudiante Sin Riesgo
```
Promedio: 15.5
Asistencia: 95%
Cursos en riesgo: 0%

Puntaje: (0.1 × 0.5) + (0.1 × 0.3) + (0.1 × 0.2) = 0.1
Categoría: 🟢 SIN RIESGO
```

### Caso 2: Estudiante en Alerta
```
Promedio: 11.8
Asistencia: 78%
Cursos en riesgo: 40%

Puntaje: (0.6 × 0.5) + (0.3 × 0.3) + (0.3 × 0.2) = 0.42
Categoría: 🟡 ALERTA AMARILLA
```

### Caso 3: Estudiante Crítico
```
Promedio: 8.5
Asistencia: 60%
Cursos en riesgo: 100%

Puntaje: (0.9 × 0.5) + (0.9 × 0.3) + (0.9 × 0.2) = 0.9
Categoría: 🔴 ALERTA ROJA
```

## 💡 Interpretación de Resultados

### Puntaje 0.1 - 0.3
- ✅ Estudiante con buen desempeño
- Mantener seguimiento regular
- Reforzar hábitos positivos

### Puntaje 0.4 - 0.6
- ⚠️ Estudiante con problemas moderados
- Requiere intervención académica
- Seguimiento más frecuente

### Puntaje 0.7 - 1.0
- 🚨 Estudiante en riesgo crítico
- Intervención inmediata necesaria
- Posible cambio de matrícula

## 📝 Notas Importantes

1. **El riesgo es dinámico** - Cambia con cada calificación o asistencia
2. **Se basa en datos actuales** - Solo considera el semestre actual
3. **Es automático** - Se calcula sin intervención manual
4. **Es objetivo** - Basado en datos, no en opiniones
5. **Genera recomendaciones** - Sugiere acciones específicas

## 🔧 Configuración del Sistema

Los pesos pueden ajustarse según la institución:

```python
# Pesos por defecto
peso_rendimiento = 0.5  (50%)
peso_asistencia = 0.3   (30%)
peso_distribucion = 0.2 (20%)

# Umbrales por defecto
umbral_amarillo = 0.4
umbral_rojo = 0.7
```

---

**El sistema de riesgo académico de SADES es automático, objetivo y basado en datos reales del estudiante.**
