-- script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
-- CHANGE DELIMITER TO //
delimiter //

CREATE
TRIGGER upd_qant
BEFORE INSERT ON orders FOR EACH ROW
BEGIN
UPDATE items SET items.quantity = items.quantity - NEW.number
WHERE items.name = NEW.item_name;
END; //

-- CHANGE DELIMITER BACK TO ;
delimiter ;
