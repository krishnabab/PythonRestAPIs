from flask import jsonify, request
from app import app

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}!")

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)  # Ensure JSON payload is parsed
    return jsonify(data)

