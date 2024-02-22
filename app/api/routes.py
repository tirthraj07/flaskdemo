from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return 'Hello World'

@api.route('/<int:apiID>')
def apiEndpoint(apiID):
    return jsonify({"api id":str(apiID)})