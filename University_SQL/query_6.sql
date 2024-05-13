"""Lista uczniów w wybranej grupie."""

SELECT "Students"."Student_id" , "Students"."Student_First_name"  , "Students"."Student_Last_name", "Grades"."Group_id" AS G
FROM "Students"
JOIN "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
WHERE "Grades"."Group_id" = 1;