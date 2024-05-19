from app import app
from flask import request, jsonify
from app.services.signup_service import Signup
from app.models.user import User
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[]
)

@app.route('/api/v1/sparfinder/signup', methods = ['POST'])
@limiter.limit("5 per hour")
def signup_controller():
			
	# create new user
	user = User(request.get_json())

	# add new user if valid
	signup = Signup()
	response = signup.signup_new_user(user)
	
	return jsonify(response)
