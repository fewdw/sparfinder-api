import jwt
from dotenv import dotenv_values

env = dotenv_values(".env")

class JWTPayloadService:
    
    def __init__(self):
        self.JWT_SECRET_KEY = env['JWT_SECRET_KEY']

    
    def get_jwt_payload(self, auth_header):
        # Get the token from the Authorization header
        if not auth_header:
            return jsonify({"error": "Authorization header missing"}), 400
        
        # The JWT token is typically sent as "Bearer <token>"
        try:
            token = auth_header.split()[1]
        except IndexError:
            return jsonify({"error": "Invalid token format"}), 400
        
        try:
            # Decode the token
            payload = jwt.decode(token, self.JWT_SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        
        # Return the payload
        return payload