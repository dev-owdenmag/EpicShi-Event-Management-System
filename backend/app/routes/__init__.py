from flask import Blueprint

# Define the blueprint
routes = Blueprint("routes", __name__)

@routes.route("/")
def home():
    return {"message": "Welcome to the Event Management System API!"}, 200
