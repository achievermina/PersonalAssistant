from DataBase.dynamoDB import Database
from API.User import User
import API.googleSignIn  as gs
import API.googleCalandar  as gc
from flask import Flask, jsonify, make_response
from flask_cors import CORS
import json
import logging, json, requests, os
import configparser
from flask import Flask, redirect, url_for, session, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from oauthlib.oauth2 import WebApplicationClient


SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

CORS(app)

@login_manager.user_loader
def load_user(user_id):
    logging.info('user get done')
    return User.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    currentUser = request.get_json()
    print(currentUser)
    user = gs.check_authentication(currentUser)
    if (user is not None):
        user.authenticated = True
        login_user(user, remember=True)
        return jsonify({'token': user.get_id()})
    else:
        return jsonify({"error": "cannot login or signup"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/test-items')
def test_items():
    db = Database()
    return '''<h2>db.test_db()</h2>'''


if __name__ == "__main__":
    app.run(ssl_context="adhoc")
