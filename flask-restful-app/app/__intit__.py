from flask import Flask
from pymongo import MongoClient
from flask_restful import Api
from routes.api import api_bp
from dotenv import load_dotenv
load_dotenv()
import os
app = Flask(__name__)

# Set the MongoDB URI and database name
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')

# Create a new PyMongo client and database instance
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo[app.config['MONGO_DBNAME']]

# Create the Flask-RESTful API
api = Api(app)

# Register the blueprint for API routes
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
