import datetime


class CNP:
    DATE_FORMAT='%Y-%m-%d'
    _date_intervals_for_natives = {
                                    '1800-1899': {
                                        'date_from': datetime.datetime(1800, 1, 1),
                                        'date_to': datetime.datetime(1899, 12, 31),
                                        'male': '3',
                                        'female': '4'
                                    },
                                    '1900-1999': {
                                        'date_from': datetime.datetime(1900, 1, 1), 
                                        'date_to': datetime.datetime(1999, 12, 31),
                                        'male': '1',
                                        'female': '2'
                                    },
                                    '2000-2099': {
                                        'date_from': datetime.datetime(2000, 1, 1), 
                                        'date_to': datetime.datetime(2099, 12, 31),
                                        'male': '5',
                                        'female': '6'
                                    }
                                }

    _county_codes = {'alba': '01', 'arad': '02', 'arges': '03', 'bacau': '04', 'bihor': '05',
                   'bistrita-nasaud': '06', 'botosani': '07', 'brasov': '08', 'braila': '09', 'buzau': '10',
                   'caras-severin': '11', 'cluj': '12', 'constanta': '13', 'covasna': '14', 'dambovita': '15',
                   'dolj': '16', 'galati': '17', 'gorj': '18', 'harghita': '19', 'hunedoara': '20',
                   'ialomita': '21', 'iasi': '22', 'ilfov': '23', 'maramures': '24', 'mehedinti': '25',
                   'mures': '26', 'neamt': '27', 'olt': '28', 'prahova': '29', 'satu mare': '30',
                   'salaj': '31', 'sibiu': '32', 'suceava': '33', 'teleorman': '34', 'timis': '35',
                   'tulcea': '36', 'vaslui': '37', 'valcea': '38', 'vrancea': '39', 'bucuresti': '40',
                   'bucuresti sector 1': '41', 'bucuresti sector 2': '42', 'bucuresti sector 3': '43',
                   'bucuresti sector 4': '44', 'bucuresti sector 5': '45', 'bucuresti sector 6': '46' ,
                   'calarasi': '51', 'giurgiu': '52'
                   }

    _romanian_characters_mapping={'a':'a',  'i': 'i', 's': 's', 't': 't'}

    _genders = ('female', 'male')

    _statuses=('native', 'resident', 'foreign')

    def __init__(self, gender: str = 'female',
                    birthdate: str = '2000-1-1', 
                    birthplace: str = 'bucuresti',
                    status: str = 'native'):
        self.gender = gender
        self.birthdate = birthdate
        self.status = status
        self.birthplace = birthplace

    @property
    def gender(self):
        return self._gender

    @property
    def birthdate(self):
        return self._birthdate

    @property
    def status(self):
        return self._status

    @property
    def birthplace(self):
        return self._birthplace

    @gender.setter
    def gender(self, value):
        if not isinstance(value, str):
            raise TypeError('gender can only be a string')
        if len(str(value).strip())==0 or value is None:
            raise ValueError('gender cannot be an empty string or None')
        if value not in CNP._genders:
            raise ValueError('gender can only be female or male')
        self._gender=value

    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise TypeError('status can only be a string')
        if len(str(value).strip())==0 or value is None:
            raise ValueError('status cannot be an empty string or None')
        if value not in CNP._statuses:
            raise KeyError('status can only be native, resident or foreign')
        self._status=value

    @birthplace.setter
    def birthplace(self, value):
        if not isinstance(value, str):
            raise TypeError('birthplace can only be a string')
        if len(str(value).strip())==0 or value is None:
            raise ValueError('birthplace cannot be an empty string or None')
        value=value.lower()
        for letter in value:
            if letter in CNP._romanian_characters_mapping.keys():
                letter=CNP._romanian_characters_mapping.get(letter)
        if value not in CNP._county_codes.keys():
            raise KeyError('birthplace can only be a county or sector from Romania')
        self._birthplace=value

    @birthdate.setter
    def birthdate(self, value):
        if not isinstance(value, str):
            raise TypeError('birthdate can only be a string')
        if len(str(value).strip())==0 or value is None:
            raise ValueError('birthdate cannot be an empty string or None')
        if datetime.datetime.strptime(value, CNP.DATE_FORMAT):
            self._birthdate=datetime.datetime.strptime(value, CNP.DATE_FORMAT)
        else:
            raise ValueError


    def _compute_gender(self):
        if not self.gender and not self.birthdate and not self.status:
            return
        if self.status==CNP._statuses[0]:
            for interval in CNP._date_intervals_for_natives.values():
                if interval.get('date_from')<=self.birthdate<=interval.get('date_to'):
                    return interval.get(self.gender)
        if self.status==CNP._statuses[1]:
            if self.gender==CNP._genders[0]:
                return '8'
            else:
                return '7'
        else:
            return '9'
    
    def _compute_year(self):
        if not self.birthdate:
            return
        return str(self.birthdate.year)[2:]


    def _compute_month(self):
        if not self.birthdate:
            return
        return str(self.birthdate.month)


    def _compute_day(self):
        if not self.birthdate:
            return
        return str(self.birthdate.day)


    def _compute_birthplace(self):
        if not self.birthplace:
            return
        return CNP._county_codes[self.birthplace]


    def _compute_NNN(self):
        for i in range(1000):
            yield i


    def _compute_C(self, value):
        pass


    def create_CNP(self):
        gen=self._compute_NNN()
        gen=str(gen)
        return self._compute_gender()+\
                self._compute_year()+\
                self._compute_month()+\
                self._compute_day()+\
                self._compute_birthplace()


class CNPValidator:
    @staticmethod
    def validate_cnp(cnp):
        CNPValidator._validate_type(cnp)
        CNPValidator._validate_digits(cnp)
        CNPValidator._validate_length(cnp)
        CNPValidator._validate_content(cnp)

    def _validate_type(cnp):
        if type(cnp)!=str:
            raise TypeError('cnp must be of type string')

    def _validate_digits(cnp):
        if not cnp.isdigit():
            raise ValueError('cnp must only contain numerical values (integers)')

    def _validate_length(cnp):
        if len(cnp)!=13:
            raise ValueError('cnp must contain exactly 13 digits')

    def _validate_content(cnp):
        if not cnp:
            raise ValueError('cnp cannot be null')
