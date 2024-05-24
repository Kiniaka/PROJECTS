import re
import json


PHONE_PATTERN = r'\b\d+\b'
NAME_PATTERN = r'([a-zA-Z])'
ALLOWED_COMMANDS = ("HELLO", "ADD", "CHANGE", "PHONE", "FIND",
                    "SHOW ALL", "GOOD BYE", "CLOSE", "EXIT", ".")


def welcome():
    welcome_string = "How can I help you?"
    end_text = print(welcome_string)
    return end_text


def add_contact():
    new_contact = {}
    contact = str(
        input("Provide your name and mobile phone number seperated by the space:"))
    contact = contact.split()
    if len(contact) == 2 and len(contact[1]) == 12:
        new_contact["name"] = contact[0].capitalize()
        new_contact['phone'] = contact[1].strip(" ")
        data.append(new_contact)
        end_text = print(f'I added contact {contact[0]}')
    else:
        wrong_contact(contact)
        add_contact()
    return


def change_phone_number():
    contact = str(
        input('Provide your name and new mobile phone number seperated by the space:'))
    contact = contact.split()
    if len(contact) == 2 and len(contact[1]) == 12:
        name = str(contact[0].capitalize())
        phone = str(contact[1].strip(" "))
        new_phone = {'name': name, 'phone': phone}
        for item in data:
            if item.get('name') == name:
                item.update(new_phone)
                print(f' The phone number has been changed for {name}')
    else:
        wrong_contact(contact)
        change_phone_number()
    print(data)
    return


def delete_phone_number():
    contact = str(
        input('Provide your name and new mobile phone number seperated by the space:'))
    contact = contact.split()
    if len(contact) == 2 and len(contact[1]) == 12:
        name = str(contact[0].capitalize())
        phone = str(contact[1].strip(" "))
        new_phone = {'name': name, 'phone': None}
        for item in data:
            if item.get('name') == name:
                item.update(new_phone)
                end_text = print(
                    f'The phone number has been removed for {name}')
    else:
        wrong_contact(contact)
        delete_phone_number()
    print(data)
    return end_text


def show_phone_number():
    show = str(input('Enter the name whose number you are looking for:'))
    lista = []
    lista = [item['phone'] for item in data if (
        (show in item.get('name')) or (show in item.get('phone')))]
    if data == [] and lista == []:
        end_text = print("The contact list is empty.")
    else:
        end_text = print(f' Phone to {show} : {lista}')
    return end_text


def find_contact_by_letter_or_digit():
    contact_date = str(input('Enter the letter or digit to find the contact:'))
    lista = []
    lista = [item for item in data if (
        (contact_date in item.get('name')) or (contact_date in item.get('phone')))]
    if lista == []:
        print('The conctact has not been found.')
    else:
        print(lista)
    return


def show_dictionary():
    if data == []:
        end_text = print('The contacts list is empty')
    else:
        end_text = print(data)
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
    elif data == 0:
        print(' The contact list is empty')
    else:
        new_phone = check_name_and_phone_format(contact[1])
        if len(new_phone) != 12:
            print('Write phone number  submit in format like this:+48000000000.')
            print(contact)
        else:
            print('Contact name should be a text.')
            print(contact)
    return


def the_end():
    end_text = "GOOD BYE!"
    end_text = print(end_text)
    if data != []:
        write_databook_in_file()
    return end_text


def write_databook_in_file():
    with open('Data_book.json', "w") as fh:
        json.dump(data, fh)
    print('Contacts has been saved!')


def read_datebook_from_file():
    with open('Data_book.json', "r") as fh:
        data = json.load(fh)
        print(f'Contacts has been load! Look at Contacts : {data}')
    return data


data = []


def main(func):
    global data
    try:
        data = read_datebook_from_file()
    except Exception:
        data = []

    decition_map = {
        "HELLO": welcome,
        "ADD": add_contact,
        "CHANGE": change_phone_number,
        "DELETE": delete_phone_number,
        "PHONE": show_phone_number,
        "FIND": find_contact_by_letter_or_digit,
        "SHOW ALL": show_dictionary,
        "SAVE": write_databook_in_file,
        "GOOD BYE": the_end,
        "CLOSE": the_end,
        "EXIT": the_end,
        ".": the_end
    }
    ask = str(input("Enter the command:"))
    ask = ask.upper()
    ask = func(ask)
    while ask:
        ask = ask.upper()
        if ask in decition_map:
            if ask in ALLOWED_COMMANDS[-4:]:
                the_end()
                return
            else:
                ask = decition_map[ask.upper()]()
                ask = str(input("Enter the command:"))
        else:
            print('Wrong command. Please try again.')
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
