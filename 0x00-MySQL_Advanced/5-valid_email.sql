-- creates a trigger that resets the attribute valid_email only when the email has been changed
-- change delimiter to mitigate conflict
delimiter //

-- trigger
CREATE TRIGGER valid_email_trig
BEFORE UPDATE ON users
FOR EACH ROW
IF NEW.email != OLD.email
THEN
SET NEW.valid_email = 0;
END IF; //

-- RESET DELIMITER
delimiter ;
