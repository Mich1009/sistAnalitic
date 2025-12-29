"""Servicio de búsqueda global"""
from app.models import Estudiante, Curso, Reporte
from sqlalchemy import or_


class SearchService:
    """Servicio para búsqueda global en el sistema"""
    
    @staticmethod
    def buscar_global(query, db, limit=20):
        """Busca en estudiantes, cursos y reportes"""
        if not query or len(query) < 2:
            return {
                'estudiantes': [],
                'cursos': [],
                'reportes': []
            }
        
        search_term = f"%{query}%"
        
        # Buscar estudiantes
        estudiantes = Estudiante.query.filter(
            or_(
                Estudiante.codigo_estudiante.ilike(search_term),
                Estudiante.nombres.ilike(search_term),
                Estudiante.apellidos.ilike(search_term),
                Estudiante.email.ilike(search_term)
            )
        ).limit(limit).all()
        
        # Buscar cursos
        cursos = Curso.query.filter(
            or_(
                Curso.codigo_curso.ilike(search_term),
                Curso.nombre_curso.ilike(search_term)
            )
        ).limit(limit).all()
        
        # Buscar reportes
        reportes = Reporte.query.filter(
            or_(
                Reporte.titulo.ilike(search_term),
                Reporte.tipo_reporte.ilike(search_term)
            )
        ).limit(limit).all()
        
        return {
            'estudiantes': estudiantes,
            'cursos': cursos,
            'reportes': reportes,
            'total': len(estudiantes) + len(cursos) + len(reportes)
        }
    
    @staticmethod
    def buscar_estudiantes(query, db, filtros=None):
        """Búsqueda avanzada de estudiantes con filtros"""
        q = Estudiante.query
        
        if query:
            search_term = f"%{query}%"
            q = q.filter(
                or_(
                    Estudiante.codigo_estudiante.ilike(search_term),
                    Estudiante.nombres.ilike(search_term),
                    Estudiante.apellidos.ilike(search_term),
                    Estudiante.email.ilike(search_term)
                )
            )
        
        # Aplicar filtros adicionales
        if filtros:
            if filtros.get('activo') is not None:
                q = q.filter(Estudiante.activo == filtros['activo'])
        
        return q
    
    @staticmethod
    def buscar_cursos(query, db, filtros=None):
        """Búsqueda avanzada de cursos con filtros"""
        q = Curso.query
        
        if query:
            search_term = f"%{query}%"
            q = q.filter(
                or_(
                    Curso.codigo_curso.ilike(search_term),
                    Curso.nombre_curso.ilike(search_term)
                )
            )
        
        if filtros:
            if filtros.get('activo') is not None:
                q = q.filter(Curso.activo == filtros['activo'])
            if filtros.get('semestre'):
                q = q.filter(Curso.semestre == filtros['semestre'])
        
        return q
