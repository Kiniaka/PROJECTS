"""Przedmioty, które prowadzi wybrany wykładowca."""

SELECT "Teachers"."Teachers_id" , "Teachers"."Teacher_First_name", "Teachers"."Teacher_Last_name", "Subjects"."Subjects_name"  AS TS
FROM "Teachers"
JOIN "Subjects" ON "Teachers"."Teachers_id" = "Subjects"."Teachers_id"
WHERE "Teachers"."Teachers_id" = 1;