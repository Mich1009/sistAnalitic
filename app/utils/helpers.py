"""Funciones auxiliares"""
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


def calcular_porcentaje_asistencia(asistencias, total_clases):
    """Calcula porcentaje de asistencia"""
    if total_clases == 0:
        return 0
    return (asistencias / total_clases) * 100


def obtener_color_riesgo(categoria):
    """Obtiene color según categoría de riesgo"""
    colores = {
        'SIN_RIESGO': 'success',
        'ALERTA_AMARILLA': 'warning',
        'ALERTA_ROJA': 'danger'
    }
    return colores.get(categoria, 'secondary')


def obtener_icono_riesgo(categoria):
    """Obtiene icono según categoría de riesgo"""
    iconos = {
        'SIN_RIESGO': '🟢',
        'ALERTA_AMARILLA': '🟡',
        'ALERTA_ROJA': '🔴'
    }
    return iconos.get(categoria, '⚪')


def formatear_fecha(fecha, formato='%d/%m/%Y'):
    """Formatea fecha"""
    if isinstance(fecha, str):
        return fecha
    return fecha.strftime(formato) if fecha else ''


def formatear_numero(numero, decimales=2):
    """Formatea número"""
    if numero is None:
        return 0
    return round(float(numero), decimales)


def obtener_rango_fechas(dias=30):
    """Obtiene rango de fechas para últimos N días"""
    hoy = datetime.now().date()
    hace_n_dias = hoy - timedelta(days=dias)
    return hace_n_dias, hoy


def paginar_resultados(query, page=1, per_page=20):
    """Pagina resultados de una query"""
    return query.paginate(page=page, per_page=per_page, error_out=False)


def obtener_semestre_actual():
    """Obtiene el semestre actual"""
    mes = datetime.now().month
    año = datetime.now().year
    
    if mes <= 6:
        return f"{año}-1"
    else:
        return f"{año}-2"


def comparar_cambios(datos_anterior, datos_nuevo):
    """Compara dos diccionarios y retorna cambios"""
    cambios = {}
    
    for clave in datos_nuevo:
        if clave not in datos_anterior:
            cambios[clave] = {
                'anterior': None,
                'nuevo': datos_nuevo[clave]
            }
        elif datos_anterior[clave] != datos_nuevo[clave]:
            cambios[clave] = {
                'anterior': datos_anterior[clave],
                'nuevo': datos_nuevo[clave]
            }
    
    return cambios


def validar_email(email):
    """Valida formato de email"""
    import re
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def validar_codigo_estudiante(codigo):
    """Valida formato de código de estudiante"""
    return len(codigo) >= 5 and len(codigo) <= 20
