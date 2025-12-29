"""Servicio de optimización de consultas"""
from sqlalchemy import and_, or_
from sqlalchemy.orm import joinedload, selectinload


class OptimizationService:
    """Servicio para optimizar consultas a base de datos"""
    
    @staticmethod
    def obtener_estudiantes_con_seguimiento(db):
        """Obtiene estudiantes con seguimiento usando eager loading"""
        from app.models import Estudiante, SeguimientoRiesgo
        
        return Estudiante.query.options(
            selectinload(Estudiante.seguimientos)
        ).all()
    
    @staticmethod
    def obtener_estudiantes_con_inscripciones(db):
        """Obtiene estudiantes con inscripciones usando eager loading"""
        from app.models import Estudiante, Inscripcion
        
        return Estudiante.query.options(
            selectinload(Estudiante.inscripciones)
        ).all()
    
    @staticmethod
    def obtener_cursos_con_inscripciones(db):
        """Obtiene cursos con inscripciones usando eager loading"""
        from app.models import Curso, Inscripcion
        
        return Curso.query.options(
            selectinload(Curso.inscripciones)
        ).all()
    
    @staticmethod
    def obtener_inscripciones_con_relaciones(db):
        """Obtiene inscripciones con todas sus relaciones"""
        from app.models import Inscripcion, Estudiante, Curso
        
        return Inscripcion.query.options(
            joinedload(Inscripcion.estudiante),
            joinedload(Inscripcion.curso)
        ).all()
    
    @staticmethod
    def obtener_estudiantes_en_riesgo_optimizado(db):
        """Obtiene estudiantes en riesgo de forma optimizada"""
        from app.models import Estudiante, SeguimientoRiesgo
        
        return db.session.query(Estudiante, SeguimientoRiesgo).options(
            joinedload(Estudiante.seguimientos)
        ).join(
            SeguimientoRiesgo, Estudiante.id == SeguimientoRiesgo.estudiante_id
        ).filter(
            SeguimientoRiesgo.categoria_riesgo != 'SIN_RIESGO'
        ).all()
    
    @staticmethod
    def crear_indice_busqueda(db):
        """Crea índices para mejorar búsquedas"""
        # Esto debería ejecutarse en una migración
        # db.session.execute("""
        # CREATE INDEX idx_estudiante_codigo ON estudiantes(codigo_estudiante);
        # CREATE INDEX idx_estudiante_nombres ON estudiantes(nombres);
        # CREATE INDEX idx_estudiante_apellidos ON estudiantes(apellidos);
        # CREATE INDEX idx_curso_codigo ON cursos(codigo_curso);
        # CREATE INDEX idx_curso_nombre ON cursos(nombre_curso);
        # """)
        pass
