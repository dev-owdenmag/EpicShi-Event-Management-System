from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Project, ClientEntry, Rsvp
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already in use"}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        role="user"
    )

    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"message": "Invalid credentials"}), 401
    
    if user.is_locked:
        return jsonify({"message": "Account is locked. Contact support at  support@iamadinkra.com"}), 403
    
    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=5))

    return jsonify({"token": access_token}), 200
    
