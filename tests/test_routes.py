"""Tests para rutas"""
import pytest
from app.models import Estudiante, Usuario
from app.extensions import db


def test_index_sin_autenticacion(client):
    """Test acceso a index sin autenticación"""
    response = client.get('/')
    assert response.status_code == 302  # Redirect a login


def test_login(client):
    """Test login"""
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    # Debería redirigir si el usuario no existe
    assert response.status_code == 200


def test_dashboard_autenticado(client, app, usuario_test):
    """Test acceso a dashboard autenticado"""
    with client:
        client.post('/auth/login', data={
            'username': 'testuser',
            'password': 'password123'
        })
        
        response = client.get('/dashboard')
        assert response.status_code == 200


def test_listar_estudiantes(client, app):
    """Test listar estudiantes"""
    with app.app_context():
        # Crear estudiante de prueba
        est = Estudiante(
            codigo_estudiante='77415003',
            nombres='Juan',
            apellidos='García',
            email='juan@example.com'
        )
        db.session.add(est)
        db.session.commit()
    
    response = client.get('/estudiantes/')
    # Sin autenticación, debería redirigir
    assert response.status_code == 302


def test_crear_estudiante_form(client):
    """Test formulario crear estudiante"""
    response = client.get('/estudiantes/crear')
    # Sin autenticación, debería redirigir
    assert response.status_code == 302
