from bank import value

def test_str():
    assert value("Hello, David") == 0
    assert value("Howdy, David") == 20
    assert value("Sup David") == 100
