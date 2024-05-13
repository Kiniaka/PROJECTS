"""Oceny uczniów w wybranej grupie z określonego przedmiotu."""

SELECT "Students"."Student_id" , "Students"."Student_First_name"  , "Students"."Student_Last_name", "Grades"."Grades"  AS G
FROM "Students"
JOIN "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
WHERE "Grades"."Group_id" = 1 and "Grades"."Subjects_id" =1;