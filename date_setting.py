from datetime import datetime, timedelta

# 현재시간 구하기
now = datetime.now()
hour = now.hour

# 오전9시 이전일 경우 전날로 셋팅
if hour < 9:
    delta = timedelta(1)
    target_date_hour = now - delta
else:
    target_date_hour = now

weekday = target_date_hour.weekday()

# 주말일 경우 이전금요일로 셋팅
if weekday >= 5:
    delta = timedelta(weekday-4)
    target_date = target_date_hour - delta
else:
    target_date = target_date_hour

def get_year():
    return target_date.strftime("%Y")

def get_month():
    return target_date.strftime("%m")

def get_day():
    return target_date.strftime("%d")
