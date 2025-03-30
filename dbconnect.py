from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://username:password@cluster1.kpemw.mongodb.net/fastapicrud"
client = MongoClient(uri, server_api = ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]