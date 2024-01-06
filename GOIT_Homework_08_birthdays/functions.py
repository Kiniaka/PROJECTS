
from datetime import datetime,timedelta
import collections

def get_birthdays_per_week(users):
    Monday_greeting_list = []
    Tuesday_greeting_list = []
    Wednesday_greeting_list = []
    Thursday_greeting_list = []
    Friday_greeting_list = []
    now = datetime.now().date()
    for item in users:
        birthday_day = item["birthday"]
        week_day = item["birthday"].strftime('%A')
        difference = birthday_day - now
        difference = int(str(difference.days))
        if   (difference) <= 7:
            if week_day == "Saturday" or week_day == "Sunday" or week_day == "Monday":
                Monday_greeting_list.append(item["name"])
            elif week_day == "Tuesday":
                Tuesday_greeting_list.append(item["name"])
            elif week_day == "Wednesday":
                Wednesday_greeting_list.append(item["name"])
            elif week_day == "Thursday":
                Thursday_greeting_list.append(item["name"])
            elif week_day == "Friday":
                Friday_greeting_list.append(item["name"])
    print(f'Monday: {Monday_greeting_list[0]}, {Monday_greeting_list[1]}, {Monday_greeting_list[2]}')
    print(f'Tuesday: {Tuesday_greeting_list[0]}')
    print(f'Wednesday: {Wednesday_greeting_list[0]}')
    print(f'Thursday: {Thursday_greeting_list[0]}')
    print(f'Friday: {Friday_greeting_list[0]}')
    return

