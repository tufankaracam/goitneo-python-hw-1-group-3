from datetime import datetime,timedelta

def get_birthdays_per_week(users):
    now = datetime.now().date()
    delta_next_week = 7 -  now.weekday()
    next_week_start = now + timedelta(days=delta_next_week) 
    next_week_end = next_week_start + timedelta(days=6)

    birthdays = {}

    current_date = next_week_start

    while (current_date <=next_week_end):
        birthdays[current_date.strftime('%A')]=[]
        current_date+=timedelta(days=1)

    for user in users:
        birthday = datetime(now.year,user['birthday'].month,user['birthday'].day).date()
        if next_week_start <=birthday <=next_week_end:
            birthdays[birthday.strftime('%A')].append(user['name']) 
            
    
    result = ''

    for k,v in birthdays.items():
        if len(v) > 0:
            names = ', '.join(v)
            result+=f'{k}: {names}\n'

    return result
