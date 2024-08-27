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

# Видалення документа з колекції cats
db.cats.delete_one({"name": "barsik"})

# Перевірка, чи документ ще існує
result = db.cats.find_one({"name": "barsik"})
print(result)

'''
None
'''
