class CNPValidator:
    def __init__(self, cnp):
        self.cnp=cnp

    @property
    def cnp(self):
        return self._cnp

    @cnp.setter
    def cnp(self, value):
        if type(value)!=str:
            raise TypeError('cnp must be of type string')
        if not value.isdigit():
            raise ValueError('cnp must only contain numerical values (integers)')
        if len(value)!=13:
            raise ValueError('cnp must contain exactly 13 digits')
        if not value:
            raise ValueError('cnp cannot be null')
        self._cnp=value