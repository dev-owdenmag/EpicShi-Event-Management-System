from flask import Blueprint, request, jsonify
from app import db
from ..models import Project
from flask_jwt_extended import jwt_required, get_jwt_identity

projects_bp = Blueprint('projects_bp', __name__)

@projects_bp.route('/projects', methods=['POST'])
@jwt_required()
def create_project():
    """Create a new project"""
    data = request.json
    client_id = get_jwt_identity()

    new_project = Project(
        client_id=client_id,
        name=data['name'],
        logo=data.get('logo', None),
        status='active'
    )

    db.session.add(new_project)
    db.session.commit()

    return jsonify({"message": "Project created successfully"}), 201

@projects_bp.route('/projects', methods=['GET'])
@jwt_required()
def get_projects():
    """Retrieve all projects for a client"""
    client_id = get_jwt_identity()
    projects = Project.query.filter_by(client_id=client_id).all()

    return jsonify([{
        "id": project.id,
        "name": project.name,
        "logo": project.logo,
        "status": project.status,
        "created_at": project.created_at
    } for project in projects]), 200

@projects_bp.route('/projects/<int:project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    """Update project details"""
    data = request.json
    project = Project.query.get(project_id)

    if not project:
        return jsonify({"message": "Project not found"}), 404

    project.name = data.get('name', project.name)
    project.logo = data.get('logo', project.logo)
    project.status = data.get('status', project.status)

    db.session.commit()
    return jsonify({"message": "Project updated successfully"}), 200

@projects_bp.route('/projects/<int:project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    """Delete a project"""
    project = Project.query.get(project_id)

    if not project:
        return jsonify({"message": "Project not found"}), 404

    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted successfully"}), 200
