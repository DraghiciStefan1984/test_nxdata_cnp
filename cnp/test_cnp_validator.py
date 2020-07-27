import pytest
import datetime
from . import CNP, __check_type, __check_is_digit, __check_length, __check_first_digit,\
            __check_location_digits, __check_day_digits, __check_month_digits,\
            __check_year_digits, __check_birthdate, __check_valid_nnn_digits, \
            __check_c_digit


def test_check_type():
    with pytest.raises(TypeError):
        __check_type(CNP(3456))

    with pytest.raises(TypeError):
        __check_type(CNP((54667)))

    with pytest.raises(TypeError):
        __check_type(CNP([3456]))

    with pytest.raises(TypeError):
        __check_type(CNP({'test':576}))

    with pytest.raises(TypeError):
        __check_type(CNP({3,5,4}))

    with pytest.raises(TypeError):
        __check_type(CNP(None))

    with pytest.raises(TypeError):
        __check_type(CNP(pytest.fixture))


def test_check_is_digit():
    with pytest.raises(ValueError):
        __check_is_digit(CNP(''))

    with pytest.raises(ValueError):
        __check_is_digit(CNP('56765n'))

    with pytest.raises(ValueError):
        __check_is_digit(CNP('6678bhb  '))


def test_check_length():
    with pytest.raises(ValueError):
        __check_length(CNP(''))

    with pytest.raises(ValueError):
        __check_length(CNP('342'))

    with pytest.raises(ValueError):
        __check_length(CNP('566789'))

    with pytest.raises(ValueError):
        __check_length(CNP('5678976754789654578'))


def test_check_first_digit():
    with pytest.raises(ValueError):
        __check_first_digit(CNP('0010987'))


def test_check_location_digits():
    with pytest.raises(ValueError):
        __check_location_digits(CNP('0000000000000'))

    with pytest.raises(ValueError):
        __check_location_digits(CNP('0000000470000'))

    with pytest.raises(ValueError):
        __check_location_digits(CNP('0000000550000'))


def test_check_day_digits():
    with pytest.raises(ValueError):
        __check_day_digits(CNP('0000033000000'))

    with pytest.raises(ValueError):
        __check_day_digits(CNP('0000000000000'))


def test_check_month_digits():
    with pytest.raises(ValueError):
        __check_month_digits(CNP('000000000000'))

    with pytest.raises(ValueError):
        __check_day_digits(CNP('0001300000000'))


def test_get_birthdate():
    assert __check_birthdate(CNP('1121214980008')) == datetime.datetime(1912, 12, 14)
    assert __check_birthdate(CNP('3121214980008')) == datetime.datetime(1812, 12, 14)
    assert __check_birthdate(CNP('7121214980008')) == datetime.datetime(1912, 12, 14)
    assert __check_birthdate(CNP('8121214980008')) == datetime.datetime(1912, 12, 14)
    assert __check_birthdate(CNP('9121214980008')) == datetime.datetime(1912, 12, 14)
    assert __check_birthdate(CNP('6121214980008')) == datetime.datetime(2012, 12, 14)

    with pytest.raises(ValueError):
        __check_birthdate(CNP('0121214980008'))


def test_check_valid_nnn_digits():
    with pytest.raises(ValueError):
        cnp=CNP('1201230888967')
        other_cnp=CNP('2201230888963')
        __check_valid_nnn_digits(cnp, other_cnp)


def test_check_c_digit():
    with pytest.raises(ValueError):
        cnp=CNP('1201230888967')
        __check_c_digit(cnp)
        