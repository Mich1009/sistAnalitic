"""Tests para servicios"""
import pytest
from app.services.search_service import SearchService
from app.services.export_service import ExportService
from app.models import Estudiante, SeguimientoRiesgo
from app.extensions import db


def test_busqueda_estudiante(app):
    """Test búsqueda de estudiante"""
    with app.app_context():
        # Crear estudiante
        est = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(est)
        db.session.commit()
        
        # Buscar
        resultados = SearchService.buscar_global('Juan', db)
        assert len(resultados['estudiantes']) > 0
        assert resultados['estudiantes'][0].nombres == 'Juan'


def test_busqueda_vacia(app):
    """Test búsqueda vacía"""
    with app.app_context():
        resultados = SearchService.buscar_global('', db)
        assert resultados['estudiantes'] == []
        assert resultados['cursos'] == []
        assert resultados['reportes'] == []


def test_busqueda_sin_resultados(app):
    """Test búsqueda sin resultados"""
    with app.app_context():
        resultados = SearchService.buscar_global('XXXXXX', db)
        assert resultados['total'] == 0


def test_exportar_excel(app):
    """Test exportación a Excel"""
    with app.app_context():
        # Crear estudiante
        est = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(est)
        db.session.commit()
        
        # Exportar
        output = ExportService.exportar_estudiantes_excel([est], {})
        assert output is not None
        assert output.getvalue() is not None


def test_exportar_csv(app):
    """Test exportación a CSV"""
    with app.app_context():
        # Crear estudiante
        est = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(est)
        db.session.commit()
        
        # Exportar
        output = ExportService.exportar_estudiantes_csv([est], {})
        assert output is not None
        contenido = output.getvalue()
        assert 'Juan' in contenido
