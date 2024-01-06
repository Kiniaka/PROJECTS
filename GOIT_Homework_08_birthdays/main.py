from datetime import datetime,timedelta
import collections


from functions import get_birthdays_per_week

if __name__ == "__main__":
    get_birthdays_per_week(users =[
    {"name":"Weronika","birthday": ((datetime.strptime('06 January 2024', '%d %B %Y')).date())},
    {"name":"Kacper","birthday": ((datetime.strptime('07 January 2024', '%d %B %Y')).date())},
    {"name":"Barbara","birthday": ((datetime.strptime('08 January 2024', '%d %B %Y')).date())},
    {"name":"Sabina","birthday": ((datetime.strptime('09 January 2024', '%d %B %Y')).date())},
    {"name":"Hanna","birthday": ((datetime.strptime('10 January 2024', '%d %B %Y')).date())},
    {"name":"Ewa","birthday": ((datetime.strptime('11 January 2024', '%d %B %Y')).date())},
    {"name":"Marcin","birthday": ((datetime.strptime('12 January 2024', '%d %B %Y')).date())},
    {"name":"Maciej","birthday": ((datetime.strptime('13 January 2024', '%d %B %Y')).date())},
    {"name":"Bartek","birthday": ((datetime.strptime('14 January 2024', '%d %B %Y')).date())},
    {"name": "Katarzyna","birthday": (datetime.strptime('15 January 2024', '%d %B %Y')).date()},
    {"name": "Krzysztof","birthday": (datetime.strptime('16 January 2024', '%d %B %Y')).date()},
    {"name": "Adam","birthday": (datetime.strptime('17 January 2024', '%d %B %Y')).date()},
    {"name": "Kazimierz","birthday": (datetime.strptime('18 January 2024', '%d %B %Y')).date()},
    {"name": "Olga","birthday": (datetime.strptime('19 January 2024', '%d %B %Y')).date()},
    {"name": "Anna","birthday": ((datetime.strptime('20 January 2024', '%d %B %Y')).date())},
    {"name": "Olga","birthday": (datetime.strptime('21 January 2024', '%d %B %Y')).date()},
    {"name":"Alicja","birthday": ((datetime.strptime('22 January 2024', '%d %B %Y')).date())},
    {"name":"Paweł","birthday": ((datetime.strptime('23 January 2024', '%d %B %Y')).date())},
    {"name":"Urszula","birthday": ((datetime.strptime('24 January 2024', '%d %B %Y')).date())},
    {"name":"Piotr","birthday": ((datetime.strptime('25 January 2024', '%d %B %Y')).date())},
    {"name":"Elżbieta","birthday": ((datetime.strptime('26 January 2024', '%d %B %Y')).date())},
    {"name":"Michał","birthday": ((datetime.strptime('27 January 2024', '%d %B %Y')).date())},
    {"name":"Aleksandra","birthday": ((datetime.strptime('28 January 2024', '%d %B %Y')).date())},
    {"name":"Antoni","birthday": ((datetime.strptime('29 January 2024', '%d %B %Y')).date())},
    {"name":"Maja","birthday": ((datetime.strptime('30 January 2024', '%d %B %Y')).date())},
    {"name":"Dominik","birthday": ((datetime.strptime('31 January 2024', '%d %B %Y')).date())}
])