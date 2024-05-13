"""Lista kursów, na które uczęszcza uczeń."""

SELECT "Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name", "Grades"."Subjects_id" AS subjects_of_Srudents
FROM "Students"
JOIN "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
where "Students"."Student_id" = 16;