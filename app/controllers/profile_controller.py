from app import app
from flask import request, jsonify
from app.services.jwt_payload_service import JWTPayloadService
from app.services.profile_service import ProfileService
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[]
)

@app.route('/api/v1/sparfinder/user-boxer-profile', methods = ['GET'])
@limiter.limit("5 per minute")
def boxer_single_profile_controller():

    auth_header = request.headers.get('Authorization')

    jwt_payload_service = JWTPayloadService()
    payload = jwt_payload_service.get_jwt_payload(auth_header)

    profile_service = ProfileService()
    return jsonify(profile_service.get_single_boxer_profile(payload))


@app.route('/api/v1/sparfinder/user-coach-profile', methods = ['GET'])
@limiter.limit("5 per minute")
def coach_single_profile_controller():

    auth_header = request.headers.get('Authorization')

    jwt_payload_service = JWTPayloadService()
    payload = jwt_payload_service.get_jwt_payload(auth_header)

    profile_service = ProfileService()
    return jsonify(profile_service.get_single_coach_profile(payload))

# ability to search all coaches
# ability to search all boxers
# ability to search all coaches and boxers
    
    
    