-- procedure
-- change from default delimiter
delimiter //

-- procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE w_d INT;
DECLARE wa_vg FLOAT;
SET w_d = (SELECT SUM(weight) FROM projects);
SELECT SUM((c.score * (p.weight / w_d))) INTO wa_vg
  FROM corrections AS c
  JOIN projects AS p
  ON c.project_id = p.id
  WHERE c.user_id = user_id;
UPDATE users SET average_score = wa_vg
  WHERE id = user_id;
END; //

-- change delimiter back to default
delimiter ;
