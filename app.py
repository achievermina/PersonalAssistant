from DataBase.dynamoDB import Database
from API.User import User
import API.googleSignIn  as gs
import API.googleCalandar  as gc
from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
import logging
from flask import Flask, redirect, url_for, session, render_template, request
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
import grpc
from gRPC import indeedclone_pb2, indeedclone_pb2_grpc

SECRET_KEY = 'development key'
app = Flask(__name__)
app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

#cors = CORS(app, resources={r"/*": {"origins": "*"}})
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#cors = CORS(app)

@login_manager.user_loader
def load_user(user_id):
    logging.info('user get done')
    return User.get(user_id)

@app.route('/login', methods=["POST"])
@cross_origin("*")
@cross_origin(origin='localhost:3000',headers=['Content-Type','Authorization'])
def login():
    print("here", request.get_json())
    googleToken = request.get_json()["googleToken"]
    myToken = request.get_json()["myToken"]

    if (myToken != ""):
        user = gs.token_Login(myToken)
    else:
        print("google Token in login function", googleToken)
        user = gs.google_token_verification(googleToken)

    if (user is not None):
        login_user(user, remember=True)
        print("user loggedin", user.id)
        response = jsonify({"ok": True, 'token': user.get_token()})
    else:
        response = jsonify({"ok": False, "error": "cannot login or signup"})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/calendar', methods=["GET"])
def get_calendar():
    print("calendar here")

    if session.get('logged_in') is not None:
        calendar = gc.GoogleCanlandarAPI()
    else:
        return jsonify({"ok": False, "error": "cannot login or signup"})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def main():
    return '''<h2>hi</h2>'''

@app.route('/indeedclone',methods=["GET"])
def search():
    print("Start service")
    searchTerm = request.get_json()["term"]
    try:
      channel = grpc.insecure_channel('localhost:3000')
      stub = indeedclone_pb2_grpc.jobServiceStub(channel)
      response = stub.Search(indeedclone_pb2.searchRequest(term=searchTerm))
      return response

    except Exception as e:
      print(e)
      return e


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
    # app.run(ssl_context="adhoc") #
    app.run(host='0.0.0.0', debug=True)

