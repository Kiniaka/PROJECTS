"""Średnia ocen wybranego ucznia wystawionych przez określonego wykładowcę."""

SELECT "Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name", "Grades"."Teachers_id", AVG("Grades"."Grades") AS average_grade
FROM "Students"
JOIN "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
where "Students"."Student_id" = 16 and "Grades"."Teachers_id" = 5
group by "Grades"."Teachers_id","Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name";