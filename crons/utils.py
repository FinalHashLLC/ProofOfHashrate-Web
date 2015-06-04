from datetime import datetime

def convert_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def datetime_to_string(time):
    return time.strftime('%Y-%m-%d %H:%M:%S')
