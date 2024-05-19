from app import app
from app.models.user import User
from dotenv import dotenv_values
import pymongo as pymongo
import uuid
import datetime
from bson import Binary
import certifi

env = dotenv_values(".env")
db_connection_string = env['MONGODB_CONNECTION_STRING']

client = pymongo.MongoClient(db_connection_string, tlsCAFile=certifi.where())
db = client.people


class Signup:
    def __init__(self):
        self.db = db

    def signup_new_user(self, user):
        
        try:
            # validate the data 
            user_is_valid = user.validate_user()
            if user_is_valid is not True:
                return user_is_valid

            # generate uuid and account creation date
            random_uuid = str(uuid.uuid4())
            account_creation_date = datetime.datetime.now().isoformat()

            # store in users
            self.db.users.insert_one({
                'uuid': random_uuid,
                'account_creation_date': account_creation_date,
                'fname': user.fname,
                'lname': user.lname,
                'username': user.username,
                'email': user.email,
                'password': user.password,
                'role': user.role
            })

            # store it in the db whether coach or boxer
            if(user.role == 'coach'):
                self.db.coaches.insert_one({
                    'username':user.username,
                    'uuid':random_uuid
                    })
            
            if(user.role == 'boxer'):
                self.db.boxers.insert_one({
                    'username':user.username,
                    'uuid':random_uuid
                    })

            response = {
                'response' : 'success',
                'type' : 'new-user-created',
                'username : ' : user.username,
                'uuid' : random_uuid
            }

        except Exception as e:

            response =  {
                'response' : 'error',
                'type' : 'not-created',
                'reason' : 'failed to reach database',
                'error' : str(e)
            }
        
        return response