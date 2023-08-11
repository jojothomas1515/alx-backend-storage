-- procedure to compute the avg for users
-- change delimeter
delimiter //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser//
-- start procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE av FLOAT;
DECLARE uids INT DEFAULT user_id;
SET av = (SELECT AVG(score) FROM corrections as c WHERE c.user_id = uids);
UPDATE users SET average_score = av WHERE id = uids;
END; //

-- revert delimiter
delimiter ;
