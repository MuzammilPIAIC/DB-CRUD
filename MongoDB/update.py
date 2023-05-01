
import pymongo

if __name__ == "__main__":
    print("welcome")
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client['test']
    collection = db['sample']

    prev = {"name": 'Laeeq'}
    next = {"$set":{"Location": "Mumbai"}}
    up = collection.update_many(prev, next)
    print(up.modified_count)

