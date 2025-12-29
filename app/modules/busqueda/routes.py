"""Rutas de búsqueda global"""
from flask import render_template, request, jsonify
from flask_login import login_required
from app.modules.busqueda import busqueda_bp
from app.services.search_service import SearchService
from app.extensions import db


@busqueda_bp.route('/global', methods=['GET'])
@login_required
def busqueda_global():
    """Página de búsqueda global"""
    query = request.args.get('q', '').strip()
    resultados = SearchService.buscar_global(query, db)
    
    return render_template('busqueda/global.html', 
                         query=query, 
                         resultados=resultados)


@busqueda_bp.route('/api/global', methods=['GET'])
@login_required
def api_busqueda_global():
    """API de búsqueda global (para autocomplete)"""
    query = request.args.get('q', '').strip()
    
    if len(query) < 2:
        return jsonify({'resultados': []})
    
    resultados = SearchService.buscar_global(query, db, limit=10)
    
    datos = {
        'estudiantes': [
            {
                'id': e.id,
                'texto': f"{e.codigo_estudiante} - {e.nombres} {e.apellidos}",
                'tipo': 'estudiante',
                'enlace': f'/estudiantes/detalle/{e.id}'
            }
            for e in resultados['estudiantes']
        ],
        'cursos': [
            {
                'id': c.id,
                'texto': f"{c.codigo_curso} - {c.nombre_curso}",
                'tipo': 'curso',
                'enlace': f'/cursos/detalle/{c.id}'
            }
            for c in resultados['cursos']
        ],
        'reportes': [
            {
                'id': r.id,
                'texto': r.titulo,
                'tipo': 'reporte',
                'enlace': f'/reportes/historial'
            }
            for r in resultados['reportes']
        ]
    }
    
    return jsonify(datos)


@busqueda_bp.route('/estudiantes', methods=['GET'])
@login_required
def buscar_estudiantes():
    """Búsqueda avanzada de estudiantes"""
    query = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    
    filtros = {
        'activo': request.args.get('activo', type=lambda x: x.lower() == 'true') if request.args.get('activo') else None
    }
    
    q = SearchService.buscar_estudiantes(query, db, filtros)
    estudiantes = q.paginate(page=page, per_page=20, error_out=False)
    
    return render_template('busqueda/estudiantes.html',
                         query=query,
                         estudiantes=estudiantes)


@busqueda_bp.route('/cursos', methods=['GET'])
@login_required
def buscar_cursos():
    """Búsqueda avanzada de cursos"""
    query = request.args.get('q', '').strip()
    page = request.args.get('page', 1, type=int)
    
    filtros = {
        'activo': request.args.get('activo', type=lambda x: x.lower() == 'true') if request.args.get('activo') else None,
        'semestre': request.args.get('semestre')
    }
    
    q = SearchService.buscar_cursos(query, db, filtros)
    cursos = q.paginate(page=page, per_page=20, error_out=False)
    
    return render_template('busqueda/cursos.html',
                         query=query,
                         cursos=cursos)
