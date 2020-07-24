import pytest
import datetime
from . import CNP


class TestCnpGender:

    #gender number testing
    def test_validate_gender_number_1990_1999(self):
        pass

    def test_validate_gender_number_1800_1899(self):
        pass

    def test_validate_gender_number_2000_2099(self):
        pass

    def test_validate_gender_number_residents(self):
        pass

    def test_validate_gender_number_foreign(self):
        pass


class TestCnpYear:
    #year number testing
    def test_validate_year_number_valid_values(self):
        pass

    def test_validate_year_number_invalid_values(self):
        pass

    def test_validate_year_number_valid_values_residents(self):
        pass

    def test_validate_year_number_invalid_values_residents(self):
        pass


class TestCnpMonth:
    #month number testing
    def test_validate_month_number_valid_values(self):
        pass

    def test_validate_month_number_invalid_values(self):
        pass


class TestCnpDay:
    #month number testing
    def test_validate_day_number_valid_values(self):
        pass

    def test_validate_day_number_invalid_values(self):
        pass
