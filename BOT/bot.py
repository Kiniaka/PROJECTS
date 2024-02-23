import functools
import re
from collections import OrderedDict
from collections import UserDict
from typing import Callable
from datetime import datetime, timedelta
import json
import re


PHONE_PATTERN = r'\b\d+\b'
NAME_PATTERN = r'([a-zA-Z])'
ALLOWED_COMMANDS = ("HELLO", "ADD", "CHANGE", "PHONE", "FIND",
                    "SHOW ALL", "GOOD BYE", "CLOSE", "EXIT", ".")


class MyException(Exception):
    pass


class AddressBook(UserDict):

    def __init__(self):
        self.records_per_page = 5
        self.current_record = 0

        super().__init__()

    def __getitem__(self, name):
        if not name in self.data.keys():
            raise MyException("The contact has not been found")
        user = self.data[name]
        return user

    def add_record(self, record):
        self.data.update({Record.Name.value: Record.contact})
        return 'Contact has been added!'

    def show_phone_number(self):
        show = str(input('Enter the name whose number you are looking for:'))
        lista = []
        lista = [item['phone'] for item in Record.data if (
            (show in item.get('name')) or (show in item.get('phone')))]
        if lista == []:
            print('The conctact has not been found.')
        else:
            print(f' Phone to {show} : {lista}')
        if Record.data == []:
            raise MyException("The contact list is empty.")

    def find_contact_by_letter_or_digit(self):
        contact_date = str(
            input('Enter the letter or digit to find the contact:'))
        lista = []
        lista = [item for item in Record.data if (
            (contact_date in item.get('name')) or (contact_date in item.get('phone')))]
        if lista == []:
            print('The conctact has not been found.')
        else:
            print(lista)
        return

    def show_dictionary(self):
        if Record.data == []:
            end_text = print('The contacts list is empty')
        else:
            end_text = print(Record.data)
        return end_text


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, value=""):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value:
            if type(value) == str and len(value) == 12 and value.isdigit():
                self.__value = value
            else:
                raise ValueError
        else:
            self.__value = ""


class Birthday(Field):
    # Birthday data has to be inputed in format like this: 07.06.1984, 20.12.1990.
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value:
            try:
                self.__value = datetime.strptime(value, '%d.%m.%Y').date()
            except:
                raise ValueError
        else:
            self.__value = ""

    def __str__(self):
        return self.value.strftime('%d.%m.%Y') if self.value else ""


class Record:

    data = []

    def __init__(self, name: Name, phone: Phone = None, birthday="") -> None:
        self.name = name
        self.phones = [phone] if phone else []
        self.birthday = Birthday(birthday)

    def welcome(self):
        welcome_string = "How can I help you?"
        end_text = print(welcome_string)
        return end_text

    def add_record(self):
        new_contact = {}
        contact = str(
            input("Provide your name and mobile phone number seperated by the space:"))
        contact = contact.split()
        if len(contact) == 2 and len(contact[1]) == 12:
            new_contact["name"] = contact[0].capitalize()
            new_contact['phone'] = contact[1].strip(" ")
            Record.data.append(new_contact)
        else:
            Record.wrong_contact(contact)
            Record.add_record(self)
        end_text = print(f'I added contact {contact[0]}')
        # print(Record.data)
        return end_text

    def change_phone_number(self):
        contact = str(
            input('Provide your name and new mobile phone number seperated by the space:'))
        contact = contact.split()
        if len(contact) == 2 and len(contact[1]) == 12:
            name = str(contact[0].capitalize())
            phone = str(contact[1].strip(" "))
            new_phone = {'name': name, 'phone': phone}
            for item in Record.data:
                if item.get('name') == name:
                    item.update(new_phone)
            end_text = print(f' The phone number has been changed for {name}')
        else:
            Record.wrong_contact(contact)
            Record.change_phone_number(self)
        print(Record.data)
        return

    def remove_phone_number(self):
        contact = str(
            input('Provide your name and new mobile phone number seperated by the space:'))
        contact = contact.split()
        if len(contact) == 2 and len(contact[1]) == 12:
            name = str(contact[0].capitalize())
            phone = str(contact[1].strip(" "))
            new_phone = {'name': name, 'phone': None}
            for item in Record.data:
                if item.get('name') == name:
                    item.update(new_phone)
        else:
            Record.wrong_contact(contact)
            Record.remove_phone_number()
        end_text = print(f'The phone number has been removed for {name}')
        print(Record.data)
        return end_text

    def check_name_and_phone_format(contact):
        name = re.findall(NAME_PATTERN, contact)
        phone = re.findall(PHONE_PATTERN, contact)
        name = ''.join(map(str, name))
        phone = "+" + phone[0]
        print(f' Name to: {name}')
        print(f'Mobile phone nr: {phone}')
        return name, phone

    def wrong_contact(contact):
        print("Wrong format of the entered data!")
        if len(contact) != 2:
            print('Remeber about seperating name and phone number by the space.')
        elif Record.data == 0:
            print(' The contact list is empty')
        else:
            new_phone = Record.check_name_and_phone_format(contact[1])
            if len(new_phone) != 12:
                print('Write phone number  submit in format like this:+48000000000.')
                print(contact)
            else:
                print('Contact name should be a text.')
                print(contact)
        return

    def the_end(self):
        end_text = "GOOD BYE!"
        end_text = print(end_text)
        if Record.data != []:
            AutoSave.write_databook_in_file()
        return end_text

    def set_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)

        return self

    def days_to_birthday(self):
        if self.birthday:

            date_now = datetime.now().date()
            year_now = date_now.year

            birthday_in_this_year = self.birthday.value.replace(year=year_now)
            birthday_in_next_year = self.birthday.value.replace(
                year=year_now + 1)

            delta1 = birthday_in_this_year - date_now
            delta2 = birthday_in_next_year - date_now

            if int(delta1.days) < 0:
                return delta2.days
            else:
                return delta1.days

        return None

    def __str__(self):
        if self.birthday:
            return f"Contact name: {Record.name}, birthday: {self.birthday}"
        else:
            return f"Contact name: {Record.name}, birthday: {None}"

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_record < len(self.data):
            if self.current_record > 0:
                input("You are pleased to push the Enter buttom to continue")

            record_values = list(self.data.values())
            results = "\n".join(map(lambda x: str(
                x), record_values[self.current_record:self.current_record + self.records_per_page]))

            self.current_record += self.records_per_page

            return results
        else:
            self.current_record = 0
            raise StopIteration


class AutoSave:
    def write_databook_in_file():
        with open('Data_book.json', "w") as fh:
            json.dump(Record.data, fh)

    def read_datebook_from_file():
        with open('Data_book.json', "r") as fh:
            json_data = json.load(fh)
            Record.data = json_data
        return json_data


def main(func):
    try:
        AutoSave.read_datebook_from_file()
    except Exception:
        Record.data = []

    decition_map = {
        "HELLO": Record.welcome,
        "ADD": Record.add_record,
        "CHANGE": Record.change_phone_number,
        "REMOVE": Record.remove_phone_number,
        "PHONE": AddressBook.show_phone_number,
        "FIND": AddressBook.find_contact_by_letter_or_digit,
        "SHOW ALL": AddressBook.show_dictionary,
        "GOOD BYE": Record.the_end,
        "CLOSE": Record.the_end,
        "EXIT": Record.the_end,
        ".": Record.the_end
    }
    ask = str(input("Enter the command:"))
    ask = ask.upper()
    ask = func(ask)
    while ask:
        ask = ask.upper()
        if ask in decition_map:
            if ask in ALLOWED_COMMANDS[-4:]:
                Record.the_end(ask)
                return
            else:
                ask = decition_map[ask](ask)
                ask = str(input("Enter the command:"))
        else:
            ask = str(input("Enter the command:"))
            continue
    return


@main
def input_error(ask):
    while ask.upper() not in ALLOWED_COMMANDS:
        print('Wrong format of the entered data!')
        print('To add new contact please write : "ADD"')
        print('To change a mobile phone number please write : "CHANGE"')
        print('To delete the phone numeber for the selected person please write: REMOVE')
        print('To find the mobile phone number to selected person please write: "PHONE"')
        print('To see all contact data please write: "SHOW ALL"')
        print('To terminate the bot work please write : "GOOD BYE" or "CLOSE" or "EXIT" or "."')
        ask = str(input("Enter the command:"))
    return ask
