single_digit_codes=set('01', '02', '03', '04', '05', '06', '07', '08', '09')


def cnp_validator(cnp: str)->bool:
    __check_type(cnp)
    __check_length(cnp)
    __check_first_digit(cnp)
    __check_location_digits(cnp)


def __check_type(cnp: str):
    if not isinstance(cnp, str):
        raise TypeError('cnp must only be a string')
    if not cnp.isdigit():
        raise ValueError('cnp must contain only digits from 0 to 9')

def __check_length(cnp: str):
    if len(cnp)!=13:
        raise ValueError('cnp must contain exactly 14 digits')

def __check_first_digit(cnp: str):
    if cnp[0]=='0':
        raise ValueError('first digit can only be a digit from 1 to 9')

def __check_location_digits(cnp: str):
    if cnp[7:9] not in single_digit_codes or not 9<int(cnp[7:9])<=46 or not 50<int(cnp[7:9])<=52:
        raise ValueError('the location digits of the cnp must be in range 01 to 46 or 51 or 52')

def __check_day_digits(cnp: str):
    if cnp[5:7] not in single_digit_codes or not 9<int(cnp[5:7])<=31:
        raise ValueError('the day digits must be in the range 01 to 31')

def __check_month_digits(cnp: str):
    if cnp[3:5] not in single_digit_codes or not 10<int(cnp[3:5])<=12:
        raise ValueError('the day digits must be in the range 01 to 12')

def __check_year_digits(cnp: str):
    if cnp[1:3] not in single_digit_codes or not 10<int(cnp[1:3])<=99 or not cnp[1:3]=='00':
        raise ValueError('the year digits must be in the range 00 to 99')

def __check_valid_birthday(cnp: str):
    pass

def __check_valid_gender_digit(cnp: str):
    pass

def __check_valid_nnn_digits(cnp: str, other_cnp: str):
    cnp_birthday_string=cnp[1:7]
    cnp_location_string=cnp[7:9]
    cnp_nnn_string=cnp[7:9]