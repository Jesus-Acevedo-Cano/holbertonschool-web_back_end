-- We are all unique
-- create table users
CREATE TABLE IF NOT EXISTS users (
id int NOT NULL AUTO_INCREMENT,
email varchar(255) NOT NULL UNIQUE,
name varchar(255),
PRIMARY KEY(id)
);
