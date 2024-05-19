from dotenv import dotenv_values
import pymongo as pymongo
import certifi
import bcrypt
import jwt
import datetime

env = dotenv_values(".env")
db_connection_string = env['MONGODB_CONNECTION_STRING']

client = pymongo.MongoClient(db_connection_string, tlsCAFile=certifi.where())
db = client.people

class Login:
    
    def __init__(self):
        self.db = db

    def login(self, user_login):
        response = {}
        try:
            username = user_login.username
            password = user_login.password

            # pull the user document
            user = self.db.users.find_one({'username':username})
            
            # check if the user exists and password matches
            if user:
                hashed_password = user.get('password', '')
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):

                    token = jwt.encode({
                        'username' : username,
                        'uuid' : user['uuid'],
                        'role' : user['role'],
                        'exp':datetime.datetime.utcnow() + datetime.timedelta(hours=4)},
                        env['JWT_SECRET_KEY'], algorithm="HS256")

                    response = {
                        'response' : 'success',
                        "type" : f"logged in",
                        'username' : username,
                        "JWT" : token
                        }
                else:
                    response = {
                        'response' : 'error',
                        'reason' : 'invalid credentials',
                    }

        except Exception as e:
            response = {
                "error": str(e),
                "reason": "failed to reach database",
                "response": "error",
                "type": "not-created"
            }

        return response