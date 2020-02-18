from Test.Calulator import Calculator

def studying_pytest():
    assert True


def test_add():
    caculator = Calculator()
    result = caculator.add(2,3)
    assert result == 5
