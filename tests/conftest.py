"""Configuración de pytest"""
import pytest
import os
from app import create_app
from app.extensions import db
from app.models import Usuario


@pytest.fixture
def app():
    """Crea una aplicación para testing"""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Cliente de prueba"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """CLI runner"""
    return app.test_cli_runner()


@pytest.fixture
def usuario_test(app):
    """Crea un usuario de prueba"""
    with app.app_context():
        usuario = Usuario(
            username='testuser',
            email='test@example.com',
            rol='docente'
        )
        usuario.set_password('password123')
        db.session.add(usuario)
        db.session.commit()
        return usuario
