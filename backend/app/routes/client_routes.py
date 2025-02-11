from flask import Blueprint, request, jsonify 
from app import db
from app.models import User, Project, ClientEntry, Rsvp
from flask_jwt_extended import jwt_required

client_bp = Blueprint('client', __name__)

@client_bp.route('/rsvp/verify', methods=['POST'])
def verify_guest():
    data = request.json
    guest_code = data['guest_code']

    guest = User.query.filter_by(username=guest_code).first()
    if not guest:
        return jsonify({"message": "Invalid guest code"}), 404
    
    return jsonify({"message": "Guest verified", "guest_name": guest.username }), 200
