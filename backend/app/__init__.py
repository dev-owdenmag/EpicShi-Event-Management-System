from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.routes import routes


db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    CORS(app)  # Enable CORS for frontend
    db.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.client_routes import client_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.rsvp_routes import rsvp_bp
    from app.routes.projects_routes import projects_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(client_bp, url_prefix="/api/client")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(rsvp_bp, url_prefix="/api/rsvp")
    app.register_blueprint(projects_bp, url_prefix="/api/projects")

    return app

