from DataBase.dynamoDB import Database

def studying_pytest():
    assert True


# def test_dbInit():
#     db = Database()
#     db.create_table("user-test")
#     item = {"id": "8888", "email": "hi@gmail.com", "name": "mina"}
#     db.add_item("user-info", item)
#     res2 = db.read_item("user-info", "8888", "hi@gmail.com")
#     assert res2['name'] == 'mina'
#     assert res2['email'] == 'hi@gmail.com'



if __name__ == '__main__':
    pass
