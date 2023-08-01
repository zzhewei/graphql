###########
# reference:https://github.com/testdrivenio/flask-spa-auth/blob/master/flask-spa-same-origin/backend/app.py
#           https://github.com/PrettyPrinted/building_user_login_system/blob/master/finish/app.py
#           https://github.com/miguelgrinberg/flasky/blob/master/app/models.py
#           https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2Fryvr_ly8f
###########
from ..model import User, db
from flask import Blueprint, request, jsonify
auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    data = {"code": 200, "success": "true", "data": "success"}
    return jsonify(data)


@auth.route("/login", methods=["POST"])
# @csrf.exempt
def login():
    """
    登入
    ---
    tags:
      - test
    parameters:
      - name: body
        in: body
        required: true
        schema:
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    produces: application/json
    responses:
      404:
        description: Page Not Fond
      500:
        description: Internal Server Error
      200:
        description: OK
    """
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user:
        if user.check_password(password):
            response = jsonify({"login": True})
            return response

    return jsonify({"login": False})



