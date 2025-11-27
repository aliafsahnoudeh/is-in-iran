from is_in_iran import is_in_iran


def test_tehran_is_inside():
    tehran = (35.6892, 51.3890)
    assert is_in_iran(*tehran) is True


def test_madrid_is_outside():
    madrid = (40.4168, -3.7038)
    assert is_in_iran(*madrid) is False
