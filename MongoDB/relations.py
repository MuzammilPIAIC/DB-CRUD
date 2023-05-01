
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")


db = client["relation_db"]
collection = db["users"]


collection.insert_many([
    {'name':'muzammil','phone':3147788844,'age':22,'email':'muzammil@jagahonline.com'},
    {'name':'osama','phone':3451188444,'age':45,'email':'osama@gmail.com'},
    {'name':'huzaifa','phone':4842115544,'age':20,'email':'huzaifa@gmail.com'},
    {'name':'hamza','phone':7884455444,'age':25,'email':'hamza@gmail.com'},
    {'name':'bilal','phone':9784455111,'age':27,'email':'bilal@gmail.com'},
    {'name':'haneef','phone':8842255444,'age':36,'email':'haneef@gmail.com'}
])





