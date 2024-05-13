"""Oceny uczniów w wybranej grupie z określonego przedmiotu na ostatnich zajęciach."""

"""Najpiew sprawdzam kiedy dodano ostatnią ocenę"""

SELECT "Grades"."Created_date"  as grades_time
FROM "Grades"
ORDER BY grades_time asc;

"""Wyświetla się : czas ostatniej dodanej oceny: ""'2024-05-10 08:15:20.258'".


SELECT
    "Students"."Student_id",
    "Students"."Student_First_name",
    "Students"."Student_Last_name",
    "Grades"."Grades",
    "Grades"."Group_id",
    "Grades"."Subjects_id",
    "Grades"."Created_date"
FROM
    "Students"
JOIN
    "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
WHERE
   "Grades"."Group_id" = 1
   AND "Grades"."Subjects_id" = 1
   AND date("Grades"."Created_date") = '2024-05-10 08:15:20.258';
