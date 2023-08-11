-- create procedure called AddBonus
-- change delimiter
-- DROP PROCEDURE IF EXISTS AddBonus;
delimiter //

-- AddBonus procedure
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(225), IN score INT)
BEGIN
DECLARE project_id INT;
IF EXISTS (SELECT id FROM projects WHERE name = project_name LIMIT 1)
THEN
SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
ELSE
INSERT INTO projects (name) VALUES (project_name);
SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
END IF;
INSERT INTO corrections (user_id, project_id, score)
VALUES (user_id, project_id, score);
END;//

delimiter ;
