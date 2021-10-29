from datetime import datetime, date

def get_now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_date_str():
    return datetime.now().strftime('%Y-%m-%d')

