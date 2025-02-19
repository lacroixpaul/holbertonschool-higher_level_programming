#!/usr/bin/python3
"""
API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)


users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400
    username = data["username"]
    password = data["password"]
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    access_token = create_access_token(identity={"username": username,
                                                 "role": user["role"]})
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()s
    return jsonify({"message": "JWT Auth: Access Granted",
                    "user": current_user}), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_role = current_user["role"]
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200
