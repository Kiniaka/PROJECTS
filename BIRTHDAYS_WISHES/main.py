from datetime import datetime, timedelta
import collections


from functions import get_birthdays_per_week

if __name__ == "__main__":
    get_birthdays_per_week(users=[
        {"name": "Weronika", "birthday": (
            (datetime.strptime('06 February 2024', '%d %B %Y')).date())},
        {"name": "Kacper", "birthday": (
            (datetime.strptime('07 February 2024', '%d %B %Y')).date())},
        {"name": "Barbara", "birthday": (
            (datetime.strptime('08 February 2024', '%d %B %Y')).date())},
        {"name": "Sabina", "birthday": (
            (datetime.strptime('09 February 2024', '%d %B %Y')).date())},
        {"name": "Hanna", "birthday": (
            (datetime.strptime('10 February 2024', '%d %B %Y')).date())},
        {"name": "Ewa", "birthday": (
            (datetime.strptime('11 February 2024', '%d %B %Y')).date())},
        {"name": "Marcin", "birthday": (
            (datetime.strptime('12 February 2024', '%d %B %Y')).date())},
        {"name": "Maciej", "birthday": (
            (datetime.strptime('13 February 2024', '%d %B %Y')).date())},
        {"name": "Bartek", "birthday": (
            (datetime.strptime('14 February 2024', '%d %B %Y')).date())},
        {"name": "Katarzyna", "birthday": (
            datetime.strptime('15 February 2024', '%d %B %Y')).date()},
        {"name": "Krzysztof", "birthday": (
            datetime.strptime('16 February 2024', '%d %B %Y')).date()},
        {"name": "Adam", "birthday": (datetime.strptime(
            '17 February 2024', '%d %B %Y')).date()},
        {"name": "Kazimierz", "birthday": (
            datetime.strptime('18 February 2024', '%d %B %Y')).date()},
        {"name": "Olga", "birthday": (datetime.strptime(
            '19 February 2024', '%d %B %Y')).date()},
        {"name": "Anna", "birthday": (
            (datetime.strptime('20 February 2024', '%d %B %Y')).date())},
        {"name": "Olga", "birthday": (datetime.strptime(
            '21 February 2024', '%d %B %Y')).date()},
        {"name": "Alicja", "birthday": (
            (datetime.strptime('22 February 2024', '%d %B %Y')).date())},
        {"name": "Paweł", "birthday": (
            (datetime.strptime('23 February 2024', '%d %B %Y')).date())},
        {"name": "Urszula", "birthday": (
            (datetime.strptime('24 February 2024', '%d %B %Y')).date())},
        {"name": "Piotr", "birthday": (
            (datetime.strptime('25 February 2024', '%d %B %Y')).date())},
        {"name": "Elżbieta", "birthday": (
            (datetime.strptime('26 February 2024', '%d %B %Y')).date())},
        {"name": "Michał", "birthday": (
            (datetime.strptime('27 February 2024', '%d %B %Y')).date())},
        {"name": "Aleksandra", "birthday": (
            (datetime.strptime('28 February 2024', '%d %B %Y')).date())},
        {"name": "Antoni", "birthday": (
            (datetime.strptime('29 February 2024', '%d %B %Y')).date())},
        {"name": "Krzysztof", "birthday": (
            (datetime.strptime('01 March 2024', '%d %B %Y')).date())}
    ])
