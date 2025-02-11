from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import jwt_required

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/clients', methods=['POST'])
@jwt_required
def add_client():
    data = request.json
    new_client = User(
        username=data['username'],
        email=data['email'],
        role="client"
    )
    new_client.set_password(data['password'])

    db.session.add(new_client)
    db.session.commit()

    return jsonify({"message": "Client created successfully"}), 201
