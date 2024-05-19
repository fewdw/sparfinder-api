import re
from app import app
from dotenv import dotenv_values
import pymongo as pymongo
import certifi

env = dotenv_values(".env")
db_connection_string = env['MONGODB_CONNECTION_STRING']

client = pymongo.MongoClient(db_connection_string, tlsCAFile=certifi.where())
db = client.people
users_collection = db.users


class Validator:
    def __init__(self):
        self.users_collection = users_collection
        pass

    def validate_name(self, name):

        valid_name = True

        if not name:
            return False
        
        if not isinstance(name, str):
            return False

        if len(name) < 3:
            return False

        if len(name) > 30:
            return False

        if not name.isalpha():
            return False

        return True


    def validate_username(self, username):
        if not username:
            return False

        if not isinstance(username, str):
            return False

        if len(username) < 5:
            return False

        if len(username) > 30:
            return False

        if not re.match(r'^[a-zA-Z0-9]+$', username):
            return False

        return True


    def validate_email(self, email):
        if not email:
            return False

        if not isinstance(email, str):
            return False

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, email):
            return False

        return True

    def validate_password(self, password):
        if not password:
            return False

        if not isinstance(password, str):
            return False

        if len(password) < 8:
            return False

        if len(password) > 30:
            return False

        pattern = r'^[a-zA-Z0-9!@#$%^&*()_+}{:;?.]+'
        if not re.match(pattern, password):
            return False

        return True

    def validate_role(self, role):
        if not role:
            return False

        if not isinstance(role, str):
            return False

        if role not in ['coach', 'boxer']:
            return False

        return True


    def validate_unique_username(self, username):
        # check if username is unique
        query = {'username': username}
        existing_user = self.users_collection.find_one(query)
        if existing_user:
            return False

        return True

    def validate_unique_email(self, email):
        # check if email is unique
        query = {'email': email}
        existing_user = self.users_collection.find_one(query)
        if existing_user:
            return False

        return True