from flask import Blueprint, request, jsonify
from app import db
from ..models import Rsvp, ClientEntry
from flask_jwt_extended import jwt_required

rsvp_bp = Blueprint('rsvp_bp', __name__)

@rsvp_bp.route('/rsvp/confirm', methods=['POST'])
def confirm_rsvp():
    """Confirm an RSVP using a guest code"""
    data = request.json
    guest_code = data.get('guest_code')

    rsvp_entry = Rsvp.query.filter_by(guest_code=guest_code).first()

    if not rsvp_entry:
        return jsonify({"message": "Invalid guest code"}), 404

    rsvp_entry.status = "confirmed"
    db.session.commit()

    return jsonify({"message": "RSVP confirmed successfully"}), 200

@rsvp_bp.route('/rsvp/decline', methods=['POST'])
def decline_rsvp():
    """Decline an RSVP using a guest code"""
    data = request.json
    guest_code = data.get('guest_code')

    rsvp_entry = Rsvp.query.filter_by(guest_code=guest_code).first()

    if not rsvp_entry:
        return jsonify({"message": "Invalid guest code"}), 404

    rsvp_entry.status = "declined"
    db.session.commit()

    return jsonify({"message": "RSVP declined successfully"}), 200

@rsvp_bp.route('/rsvp/status/<guest_code>', methods=['GET'])
def get_rsvp_status(guest_code):
    """Get RSVP status of a guest"""
    rsvp_entry = Rsvp.query.filter_by(guest_code=guest_code).first()

    if not rsvp_entry:
        return jsonify({"message": "RSVP not found"}), 404

    return jsonify({
        "guest_code": rsvp_entry.guest_code,
        "status": rsvp_entry.status,
        "created_at": rsvp_entry.created_at
    }), 200
