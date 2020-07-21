def get_days_in_range(date_from, date_to):
    dates = []
    date_to = date_to - timedelta(hours=23, minutes=59, seconds=59)
    while date_to >= date_from:
        dates.append(date_to)
        date_to = date_to - timedelta(days=1)
    dates.append(date_to)
    return dates