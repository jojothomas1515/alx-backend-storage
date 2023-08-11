-- alter table to add index on names that uses the first character
ALTER TABLE names ADD INDEX idx_name_first (name(1));
