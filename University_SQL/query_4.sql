"""Średnia ocen dla wszystkich grup, uwzględniając wszystkie oceny."""

SELECT "Grades"."Group_id", "Groups"."Group_name", AVG("Grades"."Grades") AS averages
FROM "Grades"
JOIN "Groups" ON "Grades"."Group_id" = "Groups"."Group_id"
GROUP BY "Grades"."Group_id", "Groups"."Group_name"