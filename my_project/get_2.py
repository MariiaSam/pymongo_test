import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client.book

result = db.cats.find({})
for el in result:
    print(el)

'''
(my-project-py3.11) bash-3.2$ python get.py
{'_id': ObjectId('66cdca99a6e0d50155447cdd'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
(my-project-py3.11) bash-3.2$ python get_2.py
{'_id': ObjectId('66cdca99a6e0d50155447cdd'), 'name': 'barsik', 'age': 3, 'features': ['ходить в капці', 'дає себе гладити', 'рудий']}
{'_id': ObjectId('66cdca9aa6e0d50155447cde'), 'name': 'Lama', 'age': 2, 'features': ['ходить в лоток', 'не дає себе гладити', 'сірий']}
{'_id': ObjectId('66cdca9aa6e0d50155447cdf'), 'name': 'Liza', 'age': 4, 'features': ['ходить в лоток', 'дає себе гладити', 'білий']}
'''
