
import pymongo

if __name__ == "__main__":
    print("welcome")
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client["test"]
    collection = db["sample"]
    # dic = {"name": "muzammil2", "marks":55}
    # collection.insert_one(dic)

    #######################  Add many docs ###########################

    inserThese = [
        {"name":"Laeeq", "Location": "karachi", "Maek": 212},
        {"name":"Laeeq2", "Location": "hyderabad", "Maek": 23},
        {"name":"Laeeq4", "Location": "multan", "Maek": 234},
        {"name":"Laeeq5", "Location": "lahore", "Maek": 3434},
        {"name":"Laeeq5", "Location": "Attoki", "Maek": 34},
        {"name":"Laeeq6", "Location": "Ism", "Maek": 252},
        {"name":"Laeeq3", "Location": "NOth", "Maek": 32}
    ]

    # collection.insert_many(inserThese)

    ############################# Applying Filters ##########################

    one = collection.find({"Location": "lahore"})
    #alld = collection.find({"name": "muzammil", "marks": {"$gte":600}}, {"_id":1})

    
    # alld = collection.find()

    # for item in one:
    #     print(item)
    # print(one)

    result = collection.aggregate([
        {
            "$match": {
                "Location": {
                    "$eq": 'lahore'
                },
                "Maek": {
                    '$in': [ 34, 252 ]
                }
            }
        },

        # {
        # "$count" : "total_rows_and_ther_calling"
        # }
        

    ])

    for item in result:
        print(item)

    # print("<<<<<<<: ", next(result)['name'])   

    ############################################   ###############################

    print("")
