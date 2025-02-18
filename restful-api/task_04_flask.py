#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane":
        {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john":
        {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }


@app.route('/')
def home():
    """
    Landing page
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    return list of user
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    return status
    """
    return "OK"


@app.route('/users/<username>')
def user(username):
    """
    dynamic route
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
