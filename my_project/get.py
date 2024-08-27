import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Завантаження змінних середовища з файлу .env
load_dotenv()

# Отримання URI підключення з змінної середовища
mongo_uri = os.getenv("MONGO_URI")

# Підключення до MongoDB
client = MongoClient(mongo_uri, server_api=ServerApi('1'))

db = client.book

result = db.cats.find_one({"_id": ObjectId("66cdca99a6e0d50155447cdd")})
print(result)

'''
{'_id': ObjectId('66cdca99a6e0d50155447cdd'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
'''