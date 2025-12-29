"""Servicio de notificaciones"""
from datetime import datetime
from app.extensions import db


class Notificacion(db.Model):
    """Modelo para notificaciones en la aplicación"""
    __tablename__ = 'notificaciones'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # estudiante_riesgo, reporte_generado, etc
    titulo = db.Column(db.String(200), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    leida = db.Column(db.Boolean, default=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    enlace = db.Column(db.String(500))  # Enlace a la página relevante
    
    usuario = db.relationship('Usuario', backref='notificaciones')
    
    def __repr__(self):
        return f'<Notificacion {self.tipo} - {self.usuario_id}>'


class NotificationService:
    """Servicio para gestionar notificaciones"""
    
    @staticmethod
    def crear_notificacion(usuario_id, tipo, titulo, mensaje, enlace=None):
        """Crea una nueva notificación"""
        notif = Notificacion(
            usuario_id=usuario_id,
            tipo=tipo,
            titulo=titulo,
            mensaje=mensaje,
            enlace=enlace
        )
        db.session.add(notif)
        db.session.commit()
        return notif
    
    @staticmethod
    def notificar_estudiante_en_riesgo(usuario_id, estudiante):
        """Notifica cuando un estudiante entra en riesgo"""
        titulo = f"⚠️ {estudiante.nombres} en riesgo"
        mensaje = f"El estudiante {estudiante.nombres} {estudiante.apellidos} ha entrado en riesgo académico"
        enlace = f"/estudiantes/detalle/{estudiante.id}"
        
        return NotificationService.crear_notificacion(
            usuario_id, 'estudiante_riesgo', titulo, mensaje, enlace
        )
    
    @staticmethod
    def notificar_reporte_generado(usuario_id, reporte):
        """Notifica cuando un reporte está listo"""
        titulo = f"📋 Reporte generado: {reporte.titulo}"
        mensaje = f"Tu reporte '{reporte.titulo}' ha sido generado exitosamente"
        enlace = f"/reportes/historial"
        
        return NotificationService.crear_notificacion(
            usuario_id, 'reporte_generado', titulo, mensaje, enlace
        )
    
    @staticmethod
    def notificar_estudiante_mejorado(usuario_id, estudiante):
        """Notifica cuando un estudiante mejora su situación"""
        titulo = f"✅ {estudiante.nombres} mejoró"
        mensaje = f"El estudiante {estudiante.nombres} {estudiante.apellidos} ha mejorado su situación académica"
        enlace = f"/estudiantes/detalle/{estudiante.id}"
        
        return NotificationService.crear_notificacion(
            usuario_id, 'estudiante_mejorado', titulo, mensaje, enlace
        )
    
    @staticmethod
    def obtener_notificaciones(usuario_id, no_leidas=False, limit=10):
        """Obtiene notificaciones del usuario"""
        q = Notificacion.query.filter_by(usuario_id=usuario_id)
        
        if no_leidas:
            q = q.filter_by(leida=False)
        
        return q.order_by(Notificacion.fecha_creacion.desc()).limit(limit).all()
    
    @staticmethod
    def marcar_como_leida(notificacion_id):
        """Marca una notificación como leída"""
        notif = Notificacion.query.get(notificacion_id)
        if notif:
            notif.leida = True
            db.session.commit()
        return notif
    
    @staticmethod
    def marcar_todas_como_leidas(usuario_id):
        """Marca todas las notificaciones como leídas"""
        Notificacion.query.filter_by(usuario_id=usuario_id, leida=False).update({'leida': True})
        db.session.commit()
    
    @staticmethod
    def contar_no_leidas(usuario_id):
        """Cuenta notificaciones no leídas"""
        return Notificacion.query.filter_by(usuario_id=usuario_id, leida=False).count()
