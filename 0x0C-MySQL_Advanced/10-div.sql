-- Safe divide
-- divides (and returns) the first by the second number
DELIMITER $$
CREATE FUNCTION SafeDiv ( a INT, b INT)
RETURN FLOAT
BEGIN IF b = 0 THEN RETURN 0; END IF;
RETURN a / b; 
$$
