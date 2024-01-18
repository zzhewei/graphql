from flask import Blueprint, jsonify, request

from ..model import User, db

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    data = {"code": 200, "success": "true", "data": "success"}
    return jsonify(data)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    user = User.query.filter_by(username=username).first()
    if user:
        if user.check_password(password):
            return jsonify({"login": True})

    return jsonify({"login": False})
