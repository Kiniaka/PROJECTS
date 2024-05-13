"""Średnia ocen w grupach dla wybranego przedmiotu."""

SELECT "Grades"."Group_id", "Groups"."Group_name", AVG("Grades"."Grades") AS averages
FROM "Grades"
JOIN "Subjects" ON "Grades"."Subjects_id" = "Subjects"."Subjects_id"
JOIN "Groups" ON "Grades"."Group_id" = "Groups"."Group_id"
WHERE "Subjects"."Subjects_name" = 'Maths'
GROUP BY "Grades"."Group_id", "Groups"."Group_name"