-- procedure
-- change from default delimiter
delimiter //

-- procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
-- local variables
DECLARE w_d, user_id, done INT;
DECLARE wa_vg FLOAT;
DECLARE curr CURSOR FOR SELECT id FROM users;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

-- open cursor
OPEN curr;

-- weight aggregate
SET w_d = (SELECT SUM(weight) FROM projects);

w_loop: LOOP
  FETCH curr INTO user_id;
  IF done = 1 THEN
    LEAVE w_loop;
  END IF;
  SELECT SUM((c.score * (p.weight / w_d))) INTO wa_vg
    FROM corrections AS c
    JOIN projects AS p
    ON c.project_id = p.id
    WHERE c.user_id = user_id;
  UPDATE users SET average_score = wa_vg
    WHERE id = user_id;
END LOOP;
CLOSE curr;
END; //

-- change delimiter back to default
delimiter ;
