from flask import Blueprint

busqueda_bp = Blueprint('busqueda', __name__, url_prefix='/busqueda')

from app.modules.busqueda import routes
