"""Średnia ocen wystawionych przez wykładowcę z danego przedmiotu."""

SELECT "Teachers"."Teachers_id", "Teachers"."Teacher_First_name", "Teachers"."Teacher_Last_name", AVG("Grades"."Grades") AS average_per_T
FROM "Teachers"
JOIN "Grades" ON "Teachers"."Teachers_id" = "Grades"."Teachers_id"
WHERE "Grades"."Subjects_id" = 1
GROUP  BY "Teachers"."Teachers_id";