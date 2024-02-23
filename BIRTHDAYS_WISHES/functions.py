
from datetime import datetime, timedelta
import collections


def get_birthdays_per_week(users):
    monday_greeting_list = []
    tuesday_greeting_list = []
    wednesday_greeting_list = []
    thursday_greeting_list = []
    friday_greeting_list = []
    now = datetime.now().date()
    week_day_now = now.strftime('%A')
    for item in users:
        birthday_day = item["birthday"]
        week_day = item["birthday"].strftime('%A')
        difference = birthday_day - now
        difference = int(str(difference.days))
        if 0 <= (difference) <= 7:
            if week_day == "Saturday" or week_day == "Sunday" or week_day == "Monday":
                monday_greeting_list.append(item["name"])
            elif week_day == "Tuesday":
                tuesday_greeting_list.append(item["name"])
            elif week_day == "Wednesday":
                wednesday_greeting_list.append(item["name"])
            elif week_day == "Thursday":
                thursday_greeting_list.append(item["name"])
            elif week_day == "Friday":
                friday_greeting_list.append(item["name"])

    print(f'Monday: {monday_greeting_list[0]}, {
          monday_greeting_list[1]}, {monday_greeting_list[2]}')
    print(f'Tuesday: {tuesday_greeting_list[0]}')
    print(f'Wednesday: {wednesday_greeting_list[0]}')
    print(f'Thursday: {thursday_greeting_list[0]}')
    print(f'Friday: {friday_greeting_list[0]}')

    print(f' DZISIAJ JEST: {now} {week_day_now}')
