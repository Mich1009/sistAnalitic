"""Servicio de auditoría"""
from datetime import datetime
from app.extensions import db
import json


class AuditLog(db.Model):
    """Modelo para registro de auditoría"""
    __tablename__ = 'audit_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    accion = db.Column(db.String(100), nullable=False)  # crear, editar, eliminar, ver
    entidad = db.Column(db.String(50), nullable=False)  # estudiante, curso, etc
    entidad_id = db.Column(db.Integer)
    cambios = db.Column(db.JSON)  # Qué cambió
    ip_address = db.Column(db.String(45))
    user_agent = db.Column(db.String(500))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario = db.relationship('Usuario', backref='audit_logs')
    
    def __repr__(self):
        return f'<AuditLog {self.accion} {self.entidad} - {self.usuario_id}>'


class AuditService:
    """Servicio para auditoría de cambios"""
    
    @staticmethod
    def registrar(usuario_id, accion, entidad, entidad_id=None, cambios=None, 
                  ip_address=None, user_agent=None):
        """Registra una acción en la auditoría"""
        log = AuditLog(
            usuario_id=usuario_id,
            accion=accion,
            entidad=entidad,
            entidad_id=entidad_id,
            cambios=cambios,
            ip_address=ip_address,
            user_agent=user_agent
        )
        db.session.add(log)
        db.session.commit()
        return log
    
    @staticmethod
    def registrar_creacion(usuario_id, entidad, entidad_id, datos, ip_address=None, user_agent=None):
        """Registra creación de entidad"""
        return AuditService.registrar(
            usuario_id, 'crear', entidad, entidad_id,
            {'datos_nuevos': datos},
            ip_address, user_agent
        )
    
    @staticmethod
    def registrar_edicion(usuario_id, entidad, entidad_id, cambios, ip_address=None, user_agent=None):
        """Registra edición de entidad"""
        return AuditService.registrar(
            usuario_id, 'editar', entidad, entidad_id,
            cambios,
            ip_address, user_agent
        )
    
    @staticmethod
    def registrar_eliminacion(usuario_id, entidad, entidad_id, datos, ip_address=None, user_agent=None):
        """Registra eliminación de entidad"""
        return AuditService.registrar(
            usuario_id, 'eliminar', entidad, entidad_id,
            {'datos_eliminados': datos},
            ip_address, user_agent
        )
    
    @staticmethod
    def obtener_historial(entidad=None, entidad_id=None, usuario_id=None, limit=100):
        """Obtiene historial de auditoría"""
        q = AuditLog.query
        
        if entidad:
            q = q.filter_by(entidad=entidad)
        if entidad_id:
            q = q.filter_by(entidad_id=entidad_id)
        if usuario_id:
            q = q.filter_by(usuario_id=usuario_id)
        
        return q.order_by(AuditLog.fecha.desc()).limit(limit).all()
    
    @staticmethod
    def obtener_cambios_entidad(entidad, entidad_id):
        """Obtiene todos los cambios de una entidad específica"""
        return AuditLog.query.filter_by(
            entidad=entidad,
            entidad_id=entidad_id
        ).order_by(AuditLog.fecha.desc()).all()
