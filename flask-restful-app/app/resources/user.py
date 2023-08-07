from flask_restful import Resource, reqparse
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

db = MongoClient(os.environ.get('MONGO_URI'))[ os.environ.get('MONGO_DBNAME')]

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Name field cannot be blank.")
parser.add_argument('email', type=str, required=True, help="Email field cannot be blank.")
parser.add_argument('password', type=str, required=True, help="Password field cannot be blank.")


class UsersResource(Resource):
    def get(self):
        users = list(db.users.find({}, {'_id': False}))
        return users

    def post(self):
        args = parser.parse_args()
        user_id = str(db.users.count_documents({}) + 1)
        args['id'] = user_id
        db.users.insert_one(args)
        return args, 201


class UserResource(Resource):
    def get(self, id):
        user = db.users.find_one({'id': id}, {'_id': False})
        if user:
            return user
        return {'message': 'User not found'}, 404

    def put(self, id):
        args = parser.parse_args()
        db.users.update_one({'id': id}, {'$set': args})
        return {'message': 'User updated successfully'}

    def delete(self, id):
        db.users.delete_one({'id': id})
        return {'message': 'User deleted successfully'}
