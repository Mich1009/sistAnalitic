# app/modules/estudiantes/routes.py
from flask import render_template, request, jsonify, flash, redirect, url_for, send_file
from flask_login import login_required, current_user
from . import estudiantes_bp
from app.models import Estudiante, SeguimientoRiesgo
from .forms import EstudianteForm
from datetime import datetime
from app.extensions import db
from app.services.export_service import ExportService

@estudiantes_bp.route('/')
@login_required
def index():
    """Lista de todos los estudiantes"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Query base
    estudiantes_query = Estudiante.query.filter_by(activo=True)
    
    # Búsqueda
    search = request.args.get('search', '')
    if search:
        estudiantes_query = estudiantes_query.filter(
            db.or_(
                Estudiante.nombres.ilike(f'%{search}%'),
                Estudiante.apellidos.ilike(f'%{search}%'),
                Estudiante.codigo_estudiante.ilike(f'%{search}%')
            )
        )
    
    estudiantes = estudiantes_query.paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('estudiantes/index.html', 
                         estudiantes=estudiantes,
                         search=search)

@estudiantes_bp.route('/<int:estudiante_id>')
@login_required
def detalle(estudiante_id):
    """Detalle de un estudiante específico"""
    estudiante = Estudiante.query.get_or_404(estudiante_id)
    
    # Obtener seguimientos de riesgo del estudiante
    seguimientos = SeguimientoRiesgo.query.filter_by(
        estudiante_id=estudiante_id
    ).order_by(SeguimientoRiesgo.fecha_evaluacion.desc()).all()
    
    # Procesar factores_riesgo para convertir a diccionario accesible
    for seg in seguimientos:
        if seg.factores_riesgo is None:
            seg.factores_riesgo = {}
        elif isinstance(seg.factores_riesgo, list):
            # Convertir lista de factores a diccionario
            factores_dict = {}
            for factor in seg.factores_riesgo:
                if isinstance(factor, dict):
                    nombre = factor.get('nombre', '').lower().replace(' ', '_')
                    if 'asistencia' in nombre.lower():
                        # Extraer porcentaje de la descripción
                        desc = factor.get('descripcion', '')
                        if '%' in desc:
                            try:
                                pct = float(desc.split('%')[0].split()[-1])
                                factores_dict['asistencia'] = pct
                            except:
                                pass
                    elif 'rendimiento' in nombre.lower() or 'promedio' in nombre.lower():
                        desc = factor.get('descripcion', '')
                        if '|' in desc:
                            try:
                                promedio = float(desc.split('|')[0].split(':')[-1].strip())
                                factores_dict['promedio_calificaciones'] = promedio
                            except:
                                pass
                    elif 'distribución' in nombre.lower():
                        desc = factor.get('descripcion', '')
                        if 'de' in desc:
                            try:
                                reprobadas = int(desc.split('de')[0].strip().split()[-1])
                                factores_dict['materias_reprobadas'] = reprobadas
                            except:
                                pass
            seg.factores_riesgo = factores_dict if factores_dict else {}
    
    return render_template('estudiantes/detalle.html',
                         estudiante=estudiante,
                         seguimientos=seguimientos)

@estudiantes_bp.route('/en-riesgo')
@login_required
def en_riesgo():
    """Lista de estudiantes en riesgo académico"""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # Estudiantes con seguimiento de riesgo (excluyendo SIN_RIESGO)
    estudiantes_riesgo = db.session.query(Estudiante, SeguimientoRiesgo).join(
        SeguimientoRiesgo, Estudiante.id == SeguimientoRiesgo.estudiante_id
    ).filter(
        SeguimientoRiesgo.categoria_riesgo != 'SIN_RIESGO',
        Estudiante.activo == True
    ).order_by(SeguimientoRiesgo.puntaje_riesgo.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return render_template('estudiantes/en_riesgo.html',
                         estudiantes_riesgo=estudiantes_riesgo)
    
    
@estudiantes_bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear():
    """Crear nuevo estudiante"""
    form = EstudianteForm()
    
    if form.validate_on_submit():
        try:
            # Verificar si el código de estudiante ya existe
            estudiante_existente = Estudiante.query.filter_by(
                codigo_estudiante=form.codigo_estudiante.data
            ).first()
            
            if estudiante_existente:
                flash('El código de estudiante ya existe', 'danger')
                return render_template('estudiantes/crear.html', form=form)
            
            # Verificar si el email ya existe
            email_existente = Estudiante.query.filter_by(
                email=form.email.data
            ).first()
            
            if email_existente:
                flash('El email ya está registrado', 'danger')
                return render_template('estudiantes/crear.html', form=form)
            
            # Crear nuevo estudiante
            nuevo_estudiante = Estudiante(
                codigo_estudiante=form.codigo_estudiante.data,
                nombres=form.nombres.data,
                apellidos=form.apellidos.data,
                email=form.email.data,
                telefono=form.telefono.data or None,
                fecha_inscripcion=form.fecha_inscripcion.data,
                activo=form.activo.data
            )
            
            db.session.add(nuevo_estudiante)
            db.session.commit()
            
            flash('Estudiante creado exitosamente', 'success')
            return redirect(url_for('estudiantes.index'))            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear estudiante: {str(e)}', 'danger')
    
    # Para GET request, establecer fecha actual como default
    if request.method == 'GET':
        form.fecha_inscripcion.data = datetime.utcnow().date()
    
    return render_template('estudiantes/crear.html', form=form)

@estudiantes_bp.route('/<int:estudiante_id>/editar', methods=['GET', 'POST'])
@login_required
def editar(estudiante_id):
    """Editar estudiante existente"""
    estudiante = Estudiante.query.get_or_404(estudiante_id)
    form = EstudianteForm(obj=estudiante)
    
    if form.validate_on_submit():
        try:
            # Verificar si el código de estudiante ya existe (excluyendo el actual)
            estudiante_existente = Estudiante.query.filter(
                Estudiante.codigo_estudiante == form.codigo_estudiante.data,
                Estudiante.id != estudiante_id
            ).first()
            
            if estudiante_existente:
                flash('El código de estudiante ya existe', 'danger')
                return render_template('estudiantes/editar.html', form=form, estudiante=estudiante)
            
            # Verificar si el email ya existe (excluyendo el actual)
            email_existente = Estudiante.query.filter(
                Estudiante.email == form.email.data,
                Estudiante.id != estudiante_id
            ).first()
            
            if email_existente:
                flash('El email ya está registrado', 'danger')
                return render_template('estudiantes/editar.html', form=form, estudiante=estudiante)
            
            # Actualizar estudiante
            estudiante.codigo_estudiante = form.codigo_estudiante.data
            estudiante.nombres = form.nombres.data
            estudiante.apellidos = form.apellidos.data
            estudiante.email = form.email.data
            estudiante.telefono = form.telefono.data or None
            estudiante.fecha_inscripcion = form.fecha_inscripcion.data
            estudiante.activo = form.activo.data
            
            db.session.commit()
            
            flash('Estudiante actualizado exitosamente', 'success')
            return redirect(url_for('estudiantes.detalle', estudiante_id=estudiante.id))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar estudiante: {str(e)}', 'danger')
    
    return render_template('estudiantes/editar.html', form=form, estudiante=estudiante)

@estudiantes_bp.route('/<int:estudiante_id>/eliminar', methods=['POST'])
@login_required
def eliminar(estudiante_id):
    """Eliminar estudiante"""
    try:
        estudiante = Estudiante.query.get_or_404(estudiante_id)
        
        # Verificar si tiene registros relacionados
        if estudiante.inscripciones:
            flash('No se puede eliminar el estudiante porque tiene inscripciones relacionadas', 'danger')
            return redirect(url_for('estudiantes.detalle', estudiante_id=estudiante_id))
        
        db.session.delete(estudiante)
        db.session.commit()
        
        flash('Estudiante eliminado exitosamente', 'success')
        
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar estudiante: {str(e)}', 'danger')
    
    return redirect(url_for('estudiantes.index'))


@estudiantes_bp.route('/exportar/excel')
@login_required
def exportar_excel():
    """Exporta estudiantes a Excel"""
    try:
        estudiantes = Estudiante.query.filter_by(activo=True).all()
        
        # Obtener seguimientos
        seguimientos_dict = {}
        for est in estudiantes:
            seg = SeguimientoRiesgo.query.filter_by(
                estudiante_id=est.id
            ).order_by(SeguimientoRiesgo.fecha_evaluacion.desc()).first()
            if seg:
                seguimientos_dict[est.id] = seg
        
        output = ExportService.exportar_estudiantes_excel(estudiantes, seguimientos_dict)
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f'estudiantes_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )
    except Exception as e:
        flash(f'Error exportando a Excel: {str(e)}', 'danger')
        return redirect(url_for('estudiantes.index'))


@estudiantes_bp.route('/exportar/csv')
@login_required
def exportar_csv():
    """Exporta estudiantes a CSV"""
    try:
        estudiantes = Estudiante.query.filter_by(activo=True).all()
        
        # Obtener seguimientos
        seguimientos_dict = {}
        for est in estudiantes:
            seg = SeguimientoRiesgo.query.filter_by(
                estudiante_id=est.id
            ).order_by(SeguimientoRiesgo.fecha_evaluacion.desc()).first()
            if seg:
                seguimientos_dict[est.id] = seg
        
        output = ExportService.exportar_estudiantes_csv(estudiantes, seguimientos_dict)
        
        return send_file(
            output,
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'estudiantes_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        )
    except Exception as e:
        flash(f'Error exportando a CSV: {str(e)}', 'danger')
        return redirect(url_for('estudiantes.index'))
