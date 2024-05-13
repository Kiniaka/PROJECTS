
# Przy pomocy biblioteki psycopg2 python dostaje się do bazy danych w postgresql.
import psycopg2
# Przy pomocy biblieteki fake python losowo generuje imiona i nazwiska.
from faker import Faker
import random  # Przy pomocy biblioteki random generujemy losowo wybrane dane.

fake = Faker()

# Pamiętaj o wprowadzeniu prawidłowego hasła!

db_parameters = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'secret_password',
    'host': 'localhost',
    'port': 5432
}


def connection_with_database():
    try:
        # Creating connection with the database
        conn = psycopg2.connect(**db_parameters)
        print("Połączono z bazą danych!")
        return conn
    except Exception as e:
        print(f"Błąd połączenia: {e}")
        return None


def commit_function(conn=psycopg2.connect(**db_parameters)):
    conn.commit()  # Committing inserted data.
    print("Zmiany zakomitowano w bazie danych!")


def close_connection_with_database(conn):
    conn.close()
    # Closing connection with the database.
    print("Zakończono połączenie z bazą danych!")


def creating_tables(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.
        try:

            Students_table_name = 'Students'
            Teachers_table_name = 'Teachers'
            Subjects_table_name = 'Subjects'
            Groups_table_name = 'Groups'
            Grades_table_name = 'Grades'

            insert_query_s = ("""CREATE TABLE IF NOT EXISTS "Students" (
                                "Student_id" SERIAL PRIMARY KEY,
                                "Student_First_name" VARCHAR(30) NOT NULL,
                                "Student_Last_name" VARCHAR(30) NOT NULL,
                                "Groups_id" integer,
                                "Created_date" timestamp NULL DEFAULT CURRENT_TIMESTAMP)""")

            insert_query_t = ('''CREATE TABLE IF NOT EXISTS "Teachers" (
                                "Teachers_id" serial primary key,
                                "Teacher_First_name" varchar(30) NOT NULL,
                                "Teacher_Last_name" varchar(30) NOT NULL,
                                "Created_date" timestamp NULL DEFAULT CURRENT_TIMESTAMP)''')

            insert_query_subj = ("""CREATE TABLE IF NOT EXISTS "Subjects" (
                                   "Subjects_id" serial PRIMARY KEY,
                                   "Subjects_name" VARCHAR(30) NOT NULL,
                                   "Teachers_id" INTEGER,
                                   "Created_date" TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                                    FOREIGN KEY ("Teachers_id") REFERENCES "Teachers" ("Teachers_id"));""")

            insert_query_gr = ("""CREATE TABLE IF NOT EXISTS "Groups" (
                                 "Group_id" SERIAL PRIMARY KEY,
                                 "Group_name" VARCHAR(30) NOT NULL,
                                 "Created_date" TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP);""")

            insert_query_g = ("""CREATE TABLE IF NOT EXISTS "Grades" (
                                "Grades_id" serial PRIMARY KEY,
                                "Grades" INTEGER,
                                "Group_id" INTEGER,
                                "Student_id" INTEGER,
                                "Subjects_id" INTEGER,
                                "Teachers_id" INTEGER,
                                "Created_date" TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                                FOREIGN KEY ("Student_id") REFERENCES "Students" ("Student_id"),
                                FOREIGN KEY ("Subjects_id") REFERENCES "Subjects" ("Subjects_id"),
                                FOREIGN KEY ("Teachers_id") REFERENCES "Teachers" ("Teachers_id"),
                                FOREIGN KEY ("Group_id") REFERENCES "Groups" ("Group_id"));""")

            cursor.execute(insert_query_s)  # Creating the Students table.
            commit_function(conn)
            print("Utworzono tabelę Students!")

            cursor.execute(insert_query_t)  # Creating the Teachers table.
            commit_function(conn)
            print("Utworzono tabelę Teachers!")

            cursor.execute(insert_query_subj)  # Creating the Subjects table.
            commit_function(conn)
            print("Utworzono tabelę Subjects!")

            cursor.execute(insert_query_gr)  # Creating the Groups table.
            commit_function(conn)
            print("Utworzono tabelę Groups!")

            cursor.execute(insert_query_g)  # Creating the Grades table.
            commit_function(conn)
            print("Utworzono tabelę Grades!")

        except psycopg2.Error as e:
            print(e)


def inserting_random_Students_names(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        first_name = fake.first_name()  # Creating a random first name.
        last_name = fake.last_name()  # Creating a random last name.

        insert_query = """
        INSERT INTO "Students" ("Student_First_name", "Student_Last_name")
        VALUES (%s, %s);
        """
        values = (first_name, last_name)
        # Inserting random teacher names and surnames into the Teachers table.
        cursor.execute(insert_query, values)
        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_random_Teachers_names(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        first_name = fake.first_name()  # Creating a random first name.
        last_name = fake.last_name()  # Creating a random last name.

        insert_query = """
        INSERT INTO "Teachers" ("Teacher_First_name", "Teacher_Last_name") VALUES (%s, %s);
        """
        values = (first_name, last_name)
        # Inserting random teacher names and surnames into the Teachers table.
        cursor.execute(insert_query, values)
        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_random_group_names(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        groups_names = ['A', 'B', 'C']
        for letter in groups_names:
            insert_query = """
            INSERT INTO "Groups" ("Group_name")
            VALUES (%s);
            """
            values = (letter)
            # Inserting group names into the Groups table.
            cursor.execute(insert_query, values)
            print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_subject_names(conn):
    with conn:
        cursor = conn.cursor()  # Tworzenie kursora.

        subjects_names = ['English', 'Maths', 'IT', 'Geography', 'Biology']

        for subject_name in subjects_names:
            insert_query_s = """
                INSERT INTO "Subjects" ("Subjects_name")
                VALUES (%s);
                """
            values_subject_name = (subject_name,)
            cursor.execute(insert_query_s, values_subject_name)
        print("Uzupełniono bazę danych o nazwy przedmiotów w tabeli 'Subjects'!")
        commit_function(conn)


def inserting_Teachers_id_in_Subjects_table(conn):
    with conn:
        cursor = conn.cursor()  # Tworzenie kursora.

        Teachers_id = [1, 2, 3, 4, 5]

        for s in Teachers_id:
            insert_query_TS = """UPDATE "Subjects" SET "Teachers_id" = %s WHERE "Subjects_id" = %s;"""
            values_T_id = (s, s)
            # Inserting Teachers_id in Subjects table.
            cursor.execute(insert_query_TS, values_T_id)
        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_random_Grades(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        subjects_id = [1, 2, 3, 4, 5]
        students_id = list(range(1, 31))

        for st in students_id:
            for s in subjects_id:
                grade = random.randint(1, 6)  # creating grandes from 1 to 6.
                insert_query_grades = """
                INSERT INTO "Grades" ("Grades", "Student_id", "Subjects_id")
                VALUES (%s,%s,%s)
                """
                values_grades = (grade, st, s)
                # Inserting random grades, student_id and subjects_id into the Grades table.
                cursor.execute(insert_query_grades, values_grades)
        print("Uzupełniono bazę danych o nowe dane!")
        commit_function(conn)


def inserting_Group_id_in_Students_table(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        insert_query_TS_1 = """UPDATE "Students" SET "Groups_id" = 1 WHERE "Student_id" BETWEEN 1 AND 10;"""
        insert_query_TS_2 = """UPDATE "Students" SET "Groups_id" = 2 WHERE "Student_id" BETWEEN 11 AND 20;"""
        insert_query_TS_3 = """UPDATE "Students" SET "Groups_id" = 3 WHERE "Student_id" BETWEEN 21 AND 30;"""

        cursor.execute(insert_query_TS_1)
        cursor.execute(insert_query_TS_2)
        cursor.execute(insert_query_TS_3)

        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_Group_id_in_Grades_table(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        insert_query_TS_1 = """UPDATE "Grades" SET "Group_id" = 1 WHERE "Student_id" BETWEEN 1 AND 10;"""
        insert_query_TS_2 = """UPDATE "Grades" SET "Group_id" = 2 WHERE "Student_id" BETWEEN 11 AND 20;"""
        insert_query_TS_3 = """UPDATE "Grades" SET "Group_id" = 3 WHERE "Student_id" BETWEEN 21 AND 30;"""

        # Inserting group id = 1 into the Grades table.
        cursor.execute(insert_query_TS_1)
        # Inserting group id = 2 into the Grades table.
        cursor.execute(insert_query_TS_2)
        # Inserting group id = 3 into the Grades table.
        cursor.execute(insert_query_TS_3)

        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def inserting_Teachers_id_in_Grades_table(conn):
    with conn:
        cursor = conn.cursor()  # Creating cursor.

        subjects_id = list(range(1, 6))

        for sid in subjects_id:
            insert_query_TI = """UPDATE "Grades" SET "Teachers_id" = %s WHERE "Subjects_id" = %s;"""
            values_sid = (sid, sid)
            # Inserting teacher's id into the Grades table.
            cursor.execute(insert_query_TI, values_sid)

        print("Uzupełniono bazę danych o nowe dane!")

        commit_function(conn)


def main():
    conn = psycopg2.connect(**db_parameters)

    Teachers_no = [1, 2, 3, 4, 5]
    Students_no = list(range(1, 31))
    if conn:
        creating_tables(conn)
        for t_element in Teachers_no:
            print(f' Teachers_id number: {t_element}')
            inserting_random_Teachers_names(conn)
        for s_element in Students_no:
            print(f'Students_id number {s_element}')
            inserting_random_Students_names(conn)
        inserting_random_group_names(conn)
        inserting_subject_names(conn)
        inserting_Teachers_id_in_Subjects_table(conn)
        inserting_Group_id_in_Students_table(conn)
        inserting_random_Grades(conn)
        inserting_Group_id_in_Grades_table(conn)
        inserting_Teachers_id_in_Grades_table(conn)


main()
