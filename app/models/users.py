import pymongo
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

class Users:
    def __init__(self, id=None):
        load_dotenv()
        mongocon = os.getenv('MONGO_CON')
        dbclient = pymongo.MongoClient(mongocon)
        db = dbclient[os.getenv('DATABASE')]
        self.col_users = db["users"]
        if id:
            self.id = ObjectId(id)
    
    def getAllUsers(self):
        return self.col_users.find()
    
    def addUser(self, name, country_of_origin, eta, photo, arrived, attributes):
        dict_user = {"name":name, "country_of_origin":country_of_origin, "eta":eta, "photo":photo, "arrived": arrived, "attributes":attributes}
        insertuser = self.col_users.insert_one(dict_user)
        return insertuser.inserted_id
    
    def deleteUser(self):
        query = { "_id": self.id }
        return self.col_users.delete_one(query)
    
    def updateUser(self, nama, email, alamat, telepon, biografi, website, image):
        update = { "$set": {'nama':nama, 'email':email, 'alamat':alamat, 'telepon':telepon, "biografi" : biografi, "website":website, "image":image} }
        return self.col_users.update_one({"_id":self.id}, update)