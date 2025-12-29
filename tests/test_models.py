"""Tests para modelos"""
import pytest
from app.models import Estudiante, Curso, Usuario
from app.extensions import db


def test_crear_estudiante(app):
    """Test crear estudiante"""
    with app.app_context():
        estudiante = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(estudiante)
        db.session.commit()
        
        assert estudiante.id is not None
        assert estudiante.codigo_estudiante == '77415003'
        assert estudiante.activo == True


def test_crear_curso(app):
    """Test crear curso"""
    with app.app_context():
        curso = Curso(
            codigo_curso='MAT101',
            nombre_curso='Matemáticas I',
            semestre='2025-1',
            ciclo_id=1
        )
        db.session.add(curso)
        db.session.commit()
        
        assert curso.id is not None
        assert curso.codigo_curso == 'MAT101'


def test_crear_usuario(app):
    """Test crear usuario"""
    with app.app_context():
        usuario = Usuario(
            username='testuser',
            email='test@example.com',
            rol='docente'
        )
        usuario.set_password('password123')
        db.session.add(usuario)
        db.session.commit()
        
        assert usuario.id is not None
        assert usuario.username == 'testuser'
        assert usuario.check_password('password123')


def test_estudiante_unico(app):
    """Test que código de estudiante es único"""
    with app.app_context():
        est1 = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(est1)
        db.session.commit()
        
        # Intentar crear otro con mismo código
        est2 = Estudiante(
            codigo_estudiante='77415003',
            nombres='Pedro',
            apellidos='López',
            email='pedro@example.com'
        )
        db.session.add(est2)
        
        with pytest.raises(Exception):
            db.session.commit()
