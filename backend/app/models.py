from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('superadmin', 'admin', 'client'), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Hash password before saving
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    name = db.Column(db.String(255), nullable=False)
    logo = db.Column(db.String(255), nullable=True)  # Path to uploaded logo
    status = db.Column(db.Enum('active', 'disabled'), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    client = db.relationship('User', foreign_keys=[client_id])
    admin = db.relationship('User', foreign_keys=[admin_id])


class ClientEntry(db.Model):
    __tablename__ = 'client_entries'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    guest_code = db.Column(db.String(50), unique=True, nullable=False)
    guest_name = db.Column(db.String(255), nullable=False)
    guest_email = db.Column(db.String(255), nullable=True)
    additional_data = db.Column(db.JSON, nullable=True)  # Dynamic fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    project = db.relationship('Project')
    client = db.relationship('User', foreign_keys=[client_id])


class Rsvp(db.Model):
    __tablename__ = 'rsvp'

    id = db.Column(db.Integer, primary_key=True)
    guest_code = db.Column(db.String(50), unique=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    status = db.Column(db.Enum('pending', 'confirmed', 'declined'), default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    project = db.relationship('Project')


class AdminComment(db.Model):
    __tablename__ = 'admin_comments'

    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey('client_entries.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    admin = db.relationship('User', foreign_keys=[admin_id])
    entry = db.relationship('ClientEntry')
