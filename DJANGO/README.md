## PROJEKCT DESCRIPTION:

1. The application allows you to view quotes and biographies of their authors - without logging in to the website.

2. Visitors can log in or register new account by pushing the 'LOGIN' or "Rejester here!" buttom.

3. For logged-in users, the functionality of adding a new author and a new quote and tags appears (the buttons for adding an author and a quote appear only when the user is logged in).

4. Everyone can enable viewing of a particular author's biography both from the author list page and from the quotations page - by clicking the button with the author's name and surname.After pressing the button with the author's name and surname, he or she is redirected to a page with the biography of a given author - the page has a url with the author's name and surname.

Example :
For the button named "Albert Einstein", the page has the address http://localhost:8000/authors/Albert%20Einstein/.

## TO START:

1. Open your Docker deckop.
2. Create server in POSTGRESQL by typing in command line : docker run --name myapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=019283 -d postgres.
3. Confirme by ENTER buttom.
4. Go to venv_django folder by typing in command line : cd venv_django
5. Confirme by ENTER buttom.
6. Open the virtual enviroment by typing in command line : poetry install
7. Confirme by ENTER buttom.
8. Open the virtual enviroment by typing in command line : poetry shell
9. Confirme by ENTER buttom.
10. Go to myapp folder by typing in command line : cd C:\Users\Username\Desktop\Django\new_project>
11. Confirme by ENTER buttom.
12. Run aplication on your local host by typing in command line : python manage.py runserver.
13. Open your browser and type as http adress: http://localhost:8000/homepage/
14. Confirme by ENTER buttom.
