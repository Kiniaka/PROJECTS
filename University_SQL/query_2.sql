""" Uczeń z najwyższą średnią ocen z wybranego przedmiotu."""

SELECT "Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name", AVG("Grades"."Grades") AS averages
FROM "Grades"
JOIN "Students" ON "Grades"."Student_id" = "Students"."Student_id"
JOIN "Subjects" ON "Grades"."Subjects_id" = "Subjects"."Subjects_id"
WHERE "Subjects"."Subjects_name" = 'Maths'
GROUP BY "Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name"
ORDER BY averages DESC
LIMIT 1;