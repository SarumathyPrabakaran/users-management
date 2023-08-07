from flask import Blueprint
from flask_restful import Resource, Api, reqparse
from resources.user import UsersResource, UserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Add the RESTful resource endpoints
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<id>')
