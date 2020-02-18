from flask import Flask
from DataBase import aws_controller

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/get-items')
# def get_items():
#     return jsonify(aws_controller.get_items())

@app.route('/test-items')
def test_items():
    return aws_controller.database.test_db()



if __name__ == '__main__':
    app.run()
