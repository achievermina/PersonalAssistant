from DataBase.dynamoDB import Database
from API.User import User
import API.googleSignIn  as gs
import API.googleCalandar  as gc
from flask import Flask, jsonify, make_response
from flask_cors import CORS
import logging
from flask import Flask, redirect, url_for, session, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user


SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@login_manager.user_loader
def load_user(user_id):
    logging.info('user get done')
    return User.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    user_id = request.get_json()["accesstoken"]
    print("user_id in login function",user_id)
    user = gs.google_token_verification(user_id)
    print(user.is_active())
    if (user is not None):
        login_user(user, remember=True)
        return jsonify({"ok": True, 'token': user.get_id()})
    else:
        return jsonify({"ok": False, "error": "cannot login or signup"})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def main():
    return '''<h2>hi</h2>'''

@app.route('/test-items')
def test_items():
    db = Database()
    return '''<h2>db.test_db()</h2>'''


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    return jsonify({'sum': int(data['a']) + int(data['b'])})

if __name__ == "__main__":
    logging.getLogger('flask_cors').level = logging.DEBUG
    app.run(ssl_context="adhoc") #
