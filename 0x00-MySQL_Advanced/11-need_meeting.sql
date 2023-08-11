-- create views

CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score <= 80
AND (ISNULL(last_meeting) OR (CURDATE() - last_meeting) > 30);
