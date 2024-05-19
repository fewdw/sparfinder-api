from app import app
from dotenv import dotenv_values
import pymongo as pymongo
import certifi

env = dotenv_values(".env")
db_connection_string = env['MONGODB_CONNECTION_STRING']

client = pymongo.MongoClient(db_connection_string, tlsCAFile=certifi.where())
db = client.people

class ProfileService:

    def __init__(self):
        self.db = db

    def get_single_boxer_profile(self, payload):
        
        if payload['role'] == 'coach':
            response = {
                'response' : 'error',
                'reason' : 'profile is not a boxer profile'
            }

        try: 
            if payload['role'] == 'boxer':
                boxer = self.db.boxers.find_one({'uuid': payload['uuid']}, {'_id': 0})
                response = boxer

        except Exception as e:
            response = {
                'response' : 'error',
                "reason": "failed to reach database",
                'reason' : e
            }

        return response

    def get_single_coach_profile(self, payload):
        
            if payload['role'] == 'boxer':
                response = {
                    'response' : 'error',
                    'reason' : 'profile is not a coach profile'
                }
    
            try: 
                if payload['role'] == 'coach':
                    coach = self.db.coaches.find_one({'uuid': payload['uuid']}, {'_id': 0})
                    response = coach
    
            except Exception as e:
                response = {
                    'response' : 'error',
                    "reason": "failed to reach database",
                    'reason' : e
                }
    
            return response

        