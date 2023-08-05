import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask import Flask, jsonify,request
load_dotenv()

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')


cluster = MongoClient(os.environ.get('MONGO_URI'))

db = cluster[os.environ.get('MONGO_DBNAME')]

collection = db["users"]


user_fields = ['name', 'email', 'password']


@app.route('/')
def home():
    return "Hello World!"


@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find({}))
    return jsonify(users)


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    id = int(id)
    user = collection.find_one({'_id': id}, {'_id': False})
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    if request.method=='POST':
        data = request.get_json()
       
        max_id_user = list(collection.find({}).sort("_id"))[-1]["_id"]
        
        print(max_id_user)
        data['_id'] = int(max_id_user) + 1

        collection.insert_one(data)
            
        return jsonify(data), 201
    return jsonify({'message': 'Invalid user data'}), 400

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    id = int(id)
    if (data):
        result = collection.update_one({'_id': id}, {'$set': data})
        if result.matched_count == 1:
            return jsonify({'message': 'User updated successfully'}), 200
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'message': 'Invalid user data'}), 400



@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    id = int(id)
    result = collection.delete_one({'_id': id})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")

