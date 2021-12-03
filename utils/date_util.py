import time
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def get_now_millisecond():
    return int(round(time.time() * 1000))

def get_now_str():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_date_str():
    return datetime.now().strftime('%Y-%m-%d')

# 返回 before_day_num 天前到当天的 日期date string list
def get_date_list_from_before_to_now(before_day_num):
    start_day_str = get_date_str()
    start_day = datetime.strptime(start_day_str, '%Y-%m-%d')
    before_day = start_day - relativedelta(days=before_day_num)

    day_list = []
    while before_day_num > 0:
        before_day = before_day + relativedelta(days=1)
        day_list.append(before_day.strftime('%Y-%m-%d'))
        before_day_num = before_day_num - 1

    return day_list

# 返回 before_day_num 天前到当天的 日期date string list
def get_date_list_from_now_to_after(after_day_num):
    start_day_str = get_date_str()
    start_day = datetime.strptime(start_day_str, '%Y-%m-%d')
    day_list = []
    while after_day_num > 0:
        start_day = start_day + relativedelta(days=1)
        day_list.append(start_day.strftime('%Y-%m-%d'))
        after_day_num = after_day_num - 1

    return day_list


# 返回的是时间类型
def get_date_list(start_day_str=None, end_day_str=None):
    start_day = datetime.strptime(start_day_str, '%Y-%m-%d')
    end_day = datetime.strptime(end_day_str, '%Y-%m-%d')
    day_list = []
    curr_day = start_day
    while curr_day <= end_day:
        day_list.append(curr_day)
        curr_day = curr_day + relativedelta(days=1)

    return day_list

if __name__ == '__main__':
    day_list = get_date_list_from_before_to_now(3)
    print(str(day_list))
    day_list = get_date_list_from_now_to_after(3)
    print(str(day_list))

