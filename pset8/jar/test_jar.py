from jar import Jar


def test_init():
    jar = Jar(9000, 8999)
    assert jar.capacity == 9000
    assert jar.size == 8999


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(9000, 500)
    jar.deposit(8500)
    assert jar.size == 9000


def test_withdraw():
    jar = Jar(9000, 9000)
    jar.withdraw(8500)
    assert jar.size == 500

