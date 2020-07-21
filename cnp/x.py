import datetime


d=datetime.datetime(1995, 1, 1)
date_from=datetime.datetime(1995, 1, 1)
date_to=datetime.datetime(2000, 1, 1)

print(d<date_from)
print(d<date_to)


_date_intervals_for_natives = {'1800-1899': (datetime.datetime(1800, 1, 1), datetime.datetime(1899, 12, 31)),
                                '1900-1999': (datetime.datetime(1900, 1, 1), datetime.datetime(1999, 12, 31)),
                                '2000-2099': (datetime.datetime(2000, 1, 1), datetime.datetime(2099, 12, 31)),
                                }

print(_date_intervals_for_natives.get('1800-1899')[0])