from bank import value

def test_здравствуйте():
    assert value("Здравствуйте, Боб!") == 0

def test_здрасти():
    assert value("Здрасти, Боб!") == 20

def test_hello():
    assert value("Hello, Harry!") == 100
