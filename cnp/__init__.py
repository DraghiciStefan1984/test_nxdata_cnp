import datetime

class CNP:
    _date_intervals_for_natives = {'1800-1899': (datetime.datetime(1800, 1, 1), datetime.datetime(1899, 12, 31)),
                                    '1900-1999': (datetime.datetime(1900, 1, 1), datetime.datetime(1999, 12, 31)),
                                    '2000-2099': (datetime.datetime(2000, 1, 1), datetime.datetime(2099, 12, 31)),
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

    _genders = ('female', 'male')

    _statuses=('native', 'resident', 'foreign')

    def __init__(self, gender: str = None,
                    birthdate: datetime.datetime = None, 
                    birthplace: str = None,
                    status: str = None):
        self._gender = gender
        self._birthdate = birthdate
        self._status = status
        self._birthplace = birthplace

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
        if len(str(value)).strip()==0 or value is None:
            raise ValueError('gender cannot be an empty string or None')
        if value not in CNP._genders:
            raise ValueError('gender can only be female or male')
        self._gender=gender

    @status.setter
    def status(self, value);
        if not isinstance(value, str):
            raise TypeError('status can only be a string')
        if len(str(value)).strip()==0 or value is None:
            raise ValueError('status cannot be an empty string or None')
        if value not in CNP._statuses:
            raise ValueError('status can only be native, resident or foreign')
        self._status=value

    @birthplace.setter
    def birthplace(self, value);
        if not isinstance(value, str):
            raise TypeError('birthplace can only be a string')
        if len(str(value)).strip()==0 or value is None:
            raise ValueError('birthplace cannot be an empty string or None')
        if value not in CNP._county_codes.keys():
            raise ValueError('birthplace can only be a county or sector from Romania')
        self._birthplace=value

    @birthdate.setter
    def birthdate(self, value);
        if not isinstance(value, str):
            raise TypeError('birthdate can only be a string')
        if len(str(value)).strip()==0 or value is None:
            raise ValueError('birthdate cannot be an empty string or None')
        self._birthdate=value