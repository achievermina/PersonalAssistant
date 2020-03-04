from app import app
from flask import json

# def test_add():
#     response = app.test_client().post(
#         '/add',
#         data=json.dumps({'a': 1, 'b': 2}),
#         content_type='application/json',
#     )
#
#     data = json.loads(response.get_data(as_text=True))
#
#     assert response.status_code == 200
#     assert data['sum'] == 3
#

def test_login():
    response = app.test_client().post(
        '/login',
        data=json.dumps({'accesstoken': "555"}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))
    print(data)
    assert data['ok'] == True

if __name__ == '__main__':
    #test_add()
    test_login()
