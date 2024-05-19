from app import app
import bcrypt
from app.models.validator import Validator

class User:

    def __init__(self, data):
        self.fname = data.get('fname',None)
        self.lname = data.get('lname',None)
        self.username = data.get('username',None)
        self.email = data.get('email',None)
        self.password = data.get('password',None)
        self.role = data.get('role',None)
    
    def validate_user(self):
        
        validator = Validator()

        # validate fname
        if not validator.validate_name(self.fname):
            return {"result":"error", "reason" : "Invalid first name"}

        # validate lname
        if not validator.validate_name(self.lname):
            return {"result":"error", "reason" : "Invalid last name"}

        # validate username
        if not validator.validate_username(self.username):
            return {"result":"error", "reason" : "Invalid username"}

        # validate email
        if not validator.validate_email(self.email):
            return {"result":"error", "reason" : "Invalid email"}

        # validate password
        if not validator.validate_password(self.password):
            return {"reason" : "Invalid password"}

        # username must be unique
        if not validator.validate_unique_username(self.username):
            return {"result":"error", "reason" : "Username already exists"}

        # email must be unique
        if not validator.validate_unique_email(self.email):
            return {"result":"error", "reason" : "Email already exists"}

        # validate role
        if not validator.validate_role(self.role):
            return {"result":"error", "reason" : "Invalid role"}

        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

        return True


    def to_string(self):
        return f'{self.fname} {self.lname} {self.username} {self.email} {self.password} {self.role}'
