"""5 uczniów z najwyższą średnią ocen ze wszystkich przedmiotów."""

SELECT "Students"."Student_id", "Students"."Student_First_name", "Students"."Student_Last_name", AVG("Grades"."Grades") AS averages
FROM "Students"
JOIN "Grades" ON "Students"."Student_id" = "Grades"."Student_id"
GROUP BY "Students"."Student_id"
ORDER BY averages DESC
LIMIT 5;