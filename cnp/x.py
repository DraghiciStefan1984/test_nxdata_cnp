import datetime

def check_nnn_format(cnp: str):
    min_value=0
    max_value=999
    digits=[str(i) for i in range(max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    nnn=cnp[9:13]
    return digits

print(check_nnn_format('sw'))


single_digit_codes=['01', '02', '03', '04', '05', '06', '07', '08', '09']

def __check_location_digits(cnp: str):
    min_value=1
    max_value=47
    digits=[str(i) for i in range(min_value, max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    digits.extend(['51', '52'])
    location_digits=cnp[7:9]
    if location_digits not in digits:
        raise ValueError('the location digits of the cnp must be in range 01 to 46 or 51 or 52')


def __generate_digits_range(min_value: int, max_value: int):
    digits=[str(i) for i in range(min_value, max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    return digits

def __check_year_digits(cnp: str):
    digits=__generate_digits_range(0, 99)
    digits.append('99')
    year_digits=cnp[1:3]
    if year_digits not in digits:
        raise ValueError('the year digits must be in the range 00 to 99')

def __check_day_digits(cnp: str):
    digits=__generate_digits_range(1, 32)
    day_digits=cnp[5:7]
    if day_digits not in digits:
        raise ValueError('the day digits must be in the range 01 to 31')

def __check_month_digits(cnp: str):
    digits=__generate_digits_range(1, 13)
    month_digits=cnp[3:5]
    if month_digits not in digits:
        raise ValueError('the month digits must be in the range 01 to 12')

def __check_year_digits(cnp: str):
    digits=__generate_digits_range(0, 99)
    digits.append('99')
    year_digits=cnp[1:3]
    if year_digits not in digits:
        raise ValueError('the year digits must be in the range 00 to 99')

def __get_birthdate(cnp: str) -> datetime.datetime:
    __check_year_digits(cnp)
    __check_month_digits(cnp)
    __check_day_digits(cnp)
    year=int(cnp[1:3])
    valid_year=0
    if cnp[0]=='1' or cnp[0]=='2':
        valid_year=1900+year
    elif cnp[0]=='3' or cnp[0]=='4':
        valid_year=1800+year
    elif cnp[0]=='5' or cnp[0]=='6':
        valid_year=2000+year
    else:
        raise ValueError('invalid gender value')
        return
    try:
        return datetime.datetime(valid_year, int(cnp[3:5]), int(cnp[5:7]))
    except ValueError as e:
        print(e)
        return


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


def __check_nnn_format(cnp: CNP):
    """the function will check if the nnn number is within the range 001 to 999"""
    min_value=0
    max_value=999
    digits=[str(i) for i in range(max_value)]
    digits=[(len(str(max_value))-len(digit))*'0'+str(digit) for digit in digits]
    digits.append('999')
    nnn=cnp.cnp_string[9:13]
    if nnn not in digits:
        raise ValueError('nnn number is not the range 000 - 999.') 


print(__check_nnn_format(CNP('456757478567')))