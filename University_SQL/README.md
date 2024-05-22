TO START:

1. Open commend line
2. Write in in commend line: cd University_SQL
3. Press "ENTER" button
4. Write in commend line: python """creating*and_inserting_db*.py"""
5. Press "ENTER" button

Zapytania do bazy danych, które zwrócą następujące wyniki:

1.  5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów.
2.  Uczeń z najwyższą średnią ocen z wybranego przedmiotu.
3.  Średnia ocen w grupach dla wybranego przedmiotu.
4.  Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny.
5.  Przedmioty, które prowadzi wybrany wykładowca.
6.  Lista uczniów w wybranej grupie.
7.  Oceny uczniów w wybranej grupie z określonego przedmiotu.
8.  Średnia ocen wystawionych przez wykładowcę z danego przedmiotu.
9.  Lista kursów, na które uczęszcza uczeń.
10. Lista kursów prowadzonych przez wybranego wykładowcę dla określonego ucznia.
11. Średnia ocen wybranego ucznia wystawionych przez określonego wykładowcę.
12. Oceny uczniów w wybranej grupie z określonego przedmiotu na ostatnich zajęciach.

---

Aby połączenie z bazą danych było prawidłowe należy zamienić wartości w słowniku:

---

secret_password - zamienić na prawidziwe hasło. W sktypcie ze wględu na ochronę danych zmieniona na 'secret_password'.

db_parameters = {
'dbname': 'postgres',
'user':'postgres',
'password':'secret_password',
'host':'localhost',
'port':5432
}

---

W krypcie pokazano kilka metod wstawiania danych do tabeli:

1. Uruchomienie fukcji 'main()' z pliku 'creating*and_inserting_db*' spowoduje :

   - utworzenie tabel
   - wypełnienie tych tabel danymi
     ( m.in. nazwiska i imiona randomowe, nazwy grup i przedmiotów z góry określone)
   - zapisanie w bazie danych

2. W plikach quer_n.sql gdzie n- to numer zapytań z powyższej listy :
   - zapisano komendy do wyświetlania zapytań z poziomu terminala.
