import pymongo
from app import app
app.config.from_pyfile('settings.cfg', silent=True)

class Migrate:
    def __init__(self):
        mongocon = app.config.get('MONGO_CON')
        dbclient = pymongo.MongoClient(mongocon)
        db = dbclient[app.config.get('DATABASE')]
        col_users = db["users"]
        dict_users = [
            {"name":"Taufik Hidayat", "country_of_origin":"Indonesia", "eta":"2021-07-20 09:21:20", "photo":"https://staticg.sportskeeda.com/wp-content/uploads/2012/02/taufik-hidayat.jpg", "arrived":False, "attributes":["red jacket", "blue jeans"]}
        ]
        col_users.insert_many(dict_users)

        print(dbclient.list_database_names())
        print(db.list_collection_names())

if __name__ == "__main__":
    m = Migrate()