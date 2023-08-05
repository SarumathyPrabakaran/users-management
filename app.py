import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USERN")
PASSWORD = os.getenv("PASSWORD")

print(USERNAME, PASSWORD)

cluster = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.lbdvmf4.mongodb.net/?retryWrites=true&w=majority")

db = cluster["Users"]

collection = db["users"]

data = {
    "_id": 4,
    "name" : "saru",
    "email": "saru21@joseph.com",
    "password": "something"
}


collection.insert_one(data)


