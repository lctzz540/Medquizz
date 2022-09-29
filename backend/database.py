from pymongo import MongoClient

client = MongoClient("mongodb+srv://lctzz540:Thang23062001@examapp.zow8dzs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
collection_name = db["Question"]
