TO START:

1. Open commend line
2. Write in in commend line: cd MY_BOT
3. Press "ENTER" button
4. Write in commend line: python mybot.py
5. Press "ENTER" button

PROJECT DESCRIPTION:

The project is a console assistant bot that recognizes commands entered from the keyboard and reacts in accordance with the entered command.

The bot terminates if it encounters a "."

The bot writes contacts list in file "Data_book.json", which is created while the contacts list includes one or more then one contacts.

The case of letters in the entered commands does not matter to the bot.

The bot accepts commands:

a. "HELLO", odpowiada na konsoli "How can I help you?"

b. "ADD" - bot saves the new contact ( in 'contacts_dictionary' as a dictionaries list). User have to write name and mobile phone number, always seperated by the space. The phone number should has only 12 characters in format like this : +48000000000.

c. "CHANGE" - bot save the new mobile phone number for the existing contact. The user write name and mobile phone number, always seperated by the space. The bot find the name and change the mobile phone number for this name.

d. "PHONE" - bot show the mobile phone number of the contact which name user write.

e. "FIND" - bot show the names and mobile phones of the contact after user write eighter letter which name includes or digit which is in phone number.

f. "SHOW ALL"- bot show all contacts which are saved in the contacts list.

g. "SAVE" =  bot creates new file called "Data_book.json" and saves all inputed by the user contacts in it.

h. "GOOD BYE", "CLOSE", "EXIT" - bot terminate the work and shows: "Good bye!".
