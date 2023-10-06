from django.db import models
import pymongo

class MongoConnection:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client['Usuarios']

class Texto:
    def __init__(self, mongo_connection):
        self.db_collection = mongo_connection.db["Texto"]

    @staticmethod
    def create_mongo_connection(uri):
        try:
            return MongoConnection(uri)
        except pymongo.errors.ConnectionFailure:
            raise Exception("Falha ao conectar ao MongoDB")

    def create_user(self, username, Data, titulo, Texto):
        existing_user = self.db_collection.find_one({"Texto": Texto})
        if existing_user:
            return "Nome de usuário já existe."
        user_data = {
            "Usuario": username,
            "Titulo": titulo,
            "Data": Data,
            "Texto": Texto,
        }
        try:
            self.db_collection.insert_one(user_data)
            return "Historia Criada com sucesso!"
        except pymongo.errors.DuplicateKeyError:
            return "Historia já existe."
