
import pymongo

if __name__ == "__main__":
    print("welcome")
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client['test']
    collection = db['sample']

    allDatabases = client.list_database_names()
    print(allDatabases)


    allCollection = db.list_collection_names()
    print(allCollection)