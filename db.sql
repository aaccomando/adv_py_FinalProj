CREATE DATABASE fooddb;

\connect fooddb;
--
CREATE TABLE users (
    uid SERIAL PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    pwdhash TEXT NOT NULL
);

CREATE TABLE recipes (
    recipe_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    image TEXT NOT NULL,
    ingredients JSON NOT NULL,
    url TEXT NOT NULL
);

CREATE TABLE user_recipes (
    user_recipe_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(uid),
    recipe_id INT REFERENCES recipes(recipe_id)
);
