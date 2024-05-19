from app import app
from flask import jsonify

# handle too many requests
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        'response': 'error',
        'type':'rate-limit'}), 429

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        'response': 'error',
        'type':'method-not-allowed'}), 405