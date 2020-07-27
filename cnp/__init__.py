import datetime

class CNP:
    def __init__(self, cnp_string: str, date_created: datetime.datetime=datetime.datetime.now()):
        """the CNP class will hold the cnp string and the date created"""
        self.cnp_string=cnp_string
        self.date_created=date_created

    @property
    def cnp_string(self):
        return self._cnp_string

    @property
    def date_created(self):
        return self._date_created

    @cnp_string.setter
    def cnp_string(self, value):
        self._cnp_string=value

    @date_created.setter
    def date_created(self, value):
        self._date_created=value

    def __str__(self):
        return f'CNP({self.cnp_string}) created at {self.date_created}'


"""a few helper functions"""

def __generate_digits_range(min_value: int=0, max_value: int=99):
    """ this is a helper function that will generate string representing numbers 
        within a range with leading zeros (eg. 001, 045, 00443)
    """
    digits=[str(i) for i in range(min_value, max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    return digits

def __check_day_digits(cnp: CNP):
    """the function will check if the 6th and 7th characters form a valid day number (01 to 31)"""
    digits=__generate_digits_range(1, 32)
    day_digits=cnp.cnp_string[5:7]
    if day_digits not in digits:
        raise ValueError('the day digits must be in the range 01 to 31')

def __check_month_digits(cnp: CNP):
    """the function will check if the 4th and 5th characters form a valid month number (01 to 12)"""
    digits=__generate_digits_range(1, 13)
    month_digits=cnp.cnp_string[3:5]
    if month_digits not in digits:
        raise ValueError('the month digits must be in the range 01 to 12')

def __check_year_digits(cnp: CNP):
    """the function will check if the 2nd and 3rd characters form a valid combination 
        of the last two digits of an year (00 to 99)
    """
    digits=__generate_digits_range(0, 99)
    digits.append('99')
    year_digits=cnp.cnp_string[1:3]
    if year_digits not in digits:
        raise ValueError('the year digits must be in the range 00 to 99')

def __check_birthdate(cnp: CNP) -> datetime.datetime:
    """the function will check if the characters from 2nd to the 7th form a valid
        date, taking into account the first gender digit.
    """
    __check_year_digits(cnp)
    __check_month_digits(cnp)
    __check_day_digits(cnp)
    year=int(cnp.cnp_string[1:3])
    valid_year=0
    if cnp.cnp_string[0] in '12789':
        valid_year=1900+year
    elif cnp.cnp_string[0] in '34':
        valid_year=1800+year
    elif cnp.cnp_string[0] in '56':
        valid_year=2000+year
    else:
        raise ValueError('invalid gender value')
    try:
        return datetime.datetime(valid_year, int(cnp.cnp_string[3:5]), int(cnp.cnp_string[5:7]))
    except ValueError as e:
        print(e)
        return

def __check_nnn_format(cnp: CNP):
    """the function will check if the nnn number is within the range 001 to 999"""
    min_value=0
    max_value=999
    digits=[str(i) for i in range(max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    digits.append('999')
    nnn=cnp.cnp_string[10:13]
    if nnn not in digits:
        raise ValueError('nnn number is not the range 000 - 999.') 


"""the main validation function"""
def cnp_validator(cnp: CNP, other_cnp: CNP=None)->bool:
    """the actual function that will validate the given CNP instance and will return true
        if the cnp is valid and false if cnp is invalid.
    """
    __check_type(cnp)
    __check_length(cnp)
    __check_is_digit(cnp)
    __check_first_digit(cnp)
    __check_location_digits(cnp)
    __check_valid_birtdate(cnp)
    __check_valid_nnn_digits(cnp)
    return __check_c_digit(cnp)


"""The validation functions"""
def __check_type(cnp: CNP):
    """the function will check if the value entered is of type string"""
    if type(cnp.cnp_string)!=str:
        raise TypeError('cnp must only be a string')

def __check_is_digit(cnp: CNP):
    """the function will check the characters within the string represent integers"""
    if not str(cnp.cnp_string).isdigit():
        raise ValueError('cnp must contain only digits from 0 to 9')

def __check_length(cnp: CNP):
    """a valid cnp will have no more and no less than 13 numeric characters"""
    if len(cnp.cnp_string)!=13 or len(cnp.cnp_string)==0:
        raise ValueError('cnp must contain exactly 14 digits')

def __check_first_digit(cnp: CNP):
    """the first digit, correponding to the gender, must not be 0"""
    if cnp.cnp_string[0]=='0':
        raise ValueError('first digit can only be a digit from 1 to 9')

def __check_location_digits(cnp: CNP):
    """The location code must be verified and it must be between 01 and 46, 51 or 52"""
    digits=__generate_digits_range(1, 47)
    digits.extend(['51', '52'])
    location_digits=cnp.cnp_string[7:9]
    if location_digits not in digits:
        raise ValueError('the location digits of the cnp must be in range 01 to 46 or 51 or 52')

def __check_valid_birtdate(cnp: CNP):
    try:
        birthdate=__check_birthdate(cnp)
        if not birthdate:
            raise ValueError('invalid birthdate')
    except Exception as e:
        print(e)

def __check_valid_nnn_digits(cnp: CNP, other_cnp: CNP=None):
    """the function will compare the substrings of two cnp's to see if the same nnn number
        has been assigned to two individuals in the same day in a district/county.
    """
    if other_cnp:
        if cnp.cnp_string[7:-1]==other_cnp.cnp_string[7:-1] and \
            cnp.date_created.year==other_cnp.date_created.year and \
            cnp.date_created.month==other_cnp.date_created.month and \
            cnp.date_created.day==other_cnp.date_created.day:
            print(cnp.cnp_string[7:-1])
            print(other_cnp.cnp_string[7:-1])
            raise ValueError('cannot assign the same nnn value to two CNP\'s created\
                                in the same day in the same county/district')

def __check_c_digit(cnp: CNP):
    sum_of_digits=0
    control_digit=''
    remainder=0
    check_number='279146358279'
    for i, j in zip(check_number, cnp._cnp_string[:-1]):
        sum_of_digits+=int(i)*int(j)
    remainder=sum_of_digits%11
    if remainder==10:
        control_digit='1'
    else:
        control_digit=str(remainder)
    if control_digit!=cnp._cnp_string[-1]:
        raise ValueError('control digit is incorrect')
        return False
    else:
        return True
