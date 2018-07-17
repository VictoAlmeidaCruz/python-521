from pymongo import MongoClient

client = MongoClient()
db = client['flask-app']

#for x in db.usuaros.find():
#    print(x)

