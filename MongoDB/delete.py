import pymongo

if __name__ == "__main__":
    print("welcome")
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client['test']
    collection = db['sample']

    record = {"name": 'Laeeq'}
    #next = {"$set":{"Location": "Mumbai"}}
    up = collection.delete_one(record)
    #print(up.modified_count)


    records = {"name": 'muzammil2'}
    up2 = collection.delete_many(records)
    print(up2.deleted_count)