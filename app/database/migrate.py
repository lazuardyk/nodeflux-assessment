import pymongo

class Migrate:
    def __init__(self):
        dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
        db = dbclient["vips"]
        col_users = db["users"]
        dict_users = [
            {"name":"Taufik Hidayat", "country_of_origin":"Indonesia", "eta":"2021-07-20 09:21:20", "photo":"https://staticg.sportskeeda.com/wp-content/uploads/2012/02/taufik-hidayat.jpg", "arrived":False, "attributes":["red jacket", "blue jeans"]}
        ]
        insert_user = col_users.insert_many(dict_users)
        userid_inserted = insert_user.inserted_ids

        print(dbclient.list_database_names())
        print(db.list_collection_names())

if __name__ == "__main__":
    m = Migrate()