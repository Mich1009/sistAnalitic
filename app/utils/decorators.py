"""Decoradores útiles para la aplicación"""
from functools import wraps
from flask import request, jsonify, current_app
from flask_login import current_user
from app.services.audit_service import AuditService
import logging

logger = logging.getLogger(__name__)


def audit_log(entidad, accion='editar'):
    """Decorador para registrar cambios en auditoría"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                resultado = f(*args, **kwargs)
                
                # Registrar en auditoría
                if current_user.is_authenticated:
                    AuditService.registrar(
                        usuario_id=current_user.id,
                        accion=accion,
                        entidad=entidad,
                        ip_address=request.remote_addr,
                        user_agent=request.headers.get('User-Agent', '')[:500]
                    )
                
                return resultado
            except Exception as e:
                logger.error(f"Error en audit_log: {e}")
                raise
        
        return decorated_function
    return decorator


def json_response(f):
    """Decorador para respuestas JSON"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            resultado = f(*args, **kwargs)
            if isinstance(resultado, dict):
                return jsonify(resultado)
            return resultado
        except Exception as e:
            logger.error(f"Error en json_response: {e}")
            return jsonify({'error': str(e)}), 500
    
    return decorated_function


def log_request(f):
    """Decorador para loguear requests"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logger.info(f"{request.method} {request.path} - Usuario: {current_user.username if current_user.is_authenticated else 'Anónimo'}")
        return f(*args, **kwargs)
    
    return decorated_function


def handle_errors(f):
    """Decorador para manejo de errores"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValueError as e:
            logger.warning(f"ValueError: {e}")
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            logger.error(f"Error no manejado: {e}")
            return jsonify({'error': 'Error interno del servidor'}), 500
    
    return decorated_function
