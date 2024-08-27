import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client.book

db.cats.delete_one({"name": "barsik"})

result = db.cats.find_one({"name": "barsik"})
print(result)

'''
None
'''
