# Docker_Bot

TO START:

1. Open commend line
2. Write in in commend line: cd DOCKER
3. Press "ENTER" button
4. Write in commend line: cd mynewbot
5. Press "ENTER" buttom
6. Write in commend line: docker build . -t bot/docker_bot
7. Write in commend line: docker run -it bot/docker_bot

---

## PROJECT DESCRIPTION:

The project is a console assistant bot that recognizes commands entered from the keyboard and reacts in accordance with the entered command.

The console assistant bot is run by cmd in docker conteiner using the creating by me docker image.

The bot terminates if it encounters a "."

The bot writes contacts list in file "data_save.bin", which is created while the contacts list includes one or more then one contacts.

The case of letters in the entered commands does not matter to the bot.

The bot accepts commands:

a. "HELLO", odpowiada na konsoli "How can I help you?"

b. "ADD" - bot saves the new contact ( in 'contacts_dictionary' as a dictionaries list). User have to write name and mobile phone number, always seperated by the space. The phone number should has only 12 characters in format like this : +48000000000.

c. "CHANGE" - bot save the new mobile phone number for the existing contact. The user write name and mobile phone number, always seperated by the space. The bot find the name and change the mobile phone number for this name.

d. "PHONE" - bot show the mobile phone number of the contact which name user write.

e. "FIND" - bot show the names and mobile phones of the contact after user write eighter letter which name includes or digit which is in phone number.

f. "SHOW ALL"- bot show all contacts which are saved in the contacts list.

g. "SAVE" = bot creates new file called "Data_book.json" and saves all inputed by the user contacts in it.

h. "GOOD BYE", "CLOSE", "EXIT" - bot terminate the work and shows: "Good bye!".

---

HOW I DID IT :

---

1. I have created a new repository on my GitHub 'Repositiory_name'
2. Next, I opened VSCode and open folder where I wanted to work on.
3. I wrote in the commend line : "git clone https://github.com/User_name/Repositiory_name.git"
4. I pressed ENTER.
5. To create a virtual environment,
   - I entered the following in the commend line : poetry new mynewbot
   - and pressed ENTER.
   - To creating poetry.lock file , I entered in the commend line : poetry install
   - and presed Enter.
6. To install packages with Flask , ipython and pytest to the 'pyprojects.toml' file :
   - I went to mynewbot directory by writting in the commend line: cd mynewbot/mynewbot
   - and pressed ENTER,
   - Next, I wrote: poetry shell
   - and pressed ENTER,
   - Then, to install Flask I wrote : poetry add flask
   - and pressed ENTER.
   - To install ipython as dev packege, I wrote in the commend line: poetry add ipython --dev
   - and pressed ENTER.
7. Next I created 'mynewbot.py' file and insert into it my script.
8. I have created a requirements.txt file by wroting in the commend line: poetry export --without-hashes --format=requirements.txt > requirements.txt
9. In VSCode I have created 'Dockerfile' file without extention and added insite this file instruction how to created an image.

<!--

# Polecenie Docker FROM określa podstawowy obraz kontenera.

# Podstawowy obraz to Linux z preinstalowanym python-3.11

FROM python:3.11

# Ustawiam zmienną środowiskową

ENV MY-BOT /app

# Ustawiam katalog roboczy o nazwie MY_BOT wewnątrz kontenera

WORKDIR $MY-BOT

# Kopiuje inne pliki do katalogu roboczego kontenera

COPY . .

# Instalujemy zależności wewnątrz kontenera

RUN pip install -r requirements.txt

# Oznaczamy port, na którym aplikacja działa wewnątrz kontenera

# Uruchomiamy naszą aplikację wewnątrz kontenera

CMD ["python", "mynewbot.py"] -->

10. To create image in Docker

    - I wroted in the commend line : docker build . -t bot_f/docker_bot_f

      where :

      bot - this is a name of creating image
      docker_flask - this is a name of tag of above mention image - which present version of the image (for example : to call the latest versio you can called it 'last' or 'actual')

    - and pressed enter

11. To run the conteiner with above creating image :

    - I wroted in the commend line : docker run -it bot_f/docker_bot_f
    - and pressed enter.
