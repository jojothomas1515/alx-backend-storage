-- alter table to add index on names that uses the first character and score
ALTER TABLE names ADD INDEX idx_name_first_score (name(1), score);
