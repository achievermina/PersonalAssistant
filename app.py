from flask import Flask
from flask import render_template

from DataBase import Database_Dynamo

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/get-items')
# def get_items():
#     return jsonify(aws_controller.get_items())

@app.route('/test-items')
def test_items():
    db = Database_Dynamo.database()
    return '''<h2>db.test_db()</h2>'''

@app.route('/google-signin', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    return '''<form method="GET">
                  Google email: <input type="text" name="Email"><br>
                  Password: <input type="text" name="Password"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


@app.route('/google')
def signIn():
    return render_template('googleSignIn.html')


if __name__ == '__main__':
    app.run()
