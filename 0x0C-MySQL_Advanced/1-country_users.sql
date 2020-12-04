-- In and not out
-- create table users with country
CREATE TABLE IF NOT EXISTS users (
id int NOT NULL AUTO_INCREMENT,
email varchar(255) NOT NULL UNIQUE,
name varchar(255),
country ENUM('US', 'CO', 'TN') NOT NULL,
PRIMARY KEY(id)
);
