from app import app
from flask import request, jsonify
from app.models.credentials import Credentials
from app.services.login import Login
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[]
)

@app.route('/api/v1/sparfinder/login', methods = ['POST'])
@limiter.limit("5 per hour")
def login_controller():
		
        # get user credentials
		credentials = Credentials(request.get_json())

		# create login object
		login = Login()
        # give credentials
		response = login.login(credentials)
		
		return jsonify(response)

