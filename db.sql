CREATE DATABASE fooddb;
\connect fooddb;

CREATE TABLE users(
    uid serial PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    pwdhash VARCHAR(100) NOT NULL
);

-- INSERT INTO users (firstname, lastname, email, pwdhash) VALUES (
--     'Malav', 'Patel', 'malavpatel@gmail.com', 'malavpatel'
-- );
