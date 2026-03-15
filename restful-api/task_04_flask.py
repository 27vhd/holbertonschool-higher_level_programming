#!/usr/bin/python3
"""Module for a simple API using Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Return the API status."""
    return "OK"


@app.route("/data")
def data():
    """Return a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return the full object corresponding to the provided username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary."""
    try:
        new_user = request.get_json(silent=True)
        if new_user is None:
            return jsonify({"error": "Invalid JSON"}), 400
        if "username" not in new_user:
            return jsonify({"error": "Username is required"}), 400
        username = new_user["username"]
        if username in users:
            return jsonify({"error": "Username already exists"}), 409
        users[username] = new_user
        return jsonify({"message": "User added", "user": new_user}), 201
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
