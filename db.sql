DROP TABLE IF EXISTS movies cascade;
DROP TABLE IF EXISTS users cascade;
DROP TYPE IF EXISTS genre;
DROP TYPE IF EXISTS usertype;

-- CREATE TYPE
CREATE TYPE genre AS ENUM (
    'ADVENTURE',
    'HORROR',
    'COMEDY',
    'ACTION',
    'SPORTS'
);

-- CREATE TYPE
DROP TYPE IF EXISTS usertype;
CREATE TYPE usertype AS ENUM (
    'ADMINISTRATOR',
    'USER'
);

-- CREATE TABLE

CREATE TABLE movies (
    movie_id VARCHAR PRIMARY KEY NOT NULL,
    title VARCHAR NOT NULL,
    release_year SMALLINT,
    genre genre,
    price NUMERIC(4, 2)
);
-- CREATE TABLE

CREATE TABLE users (
    user_id VARCHAR PRIMARY KEY NOT NULL,
    name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    age integer,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    user_type usertype DEFAULT 'USER'
);

-- LOAD DATAS
INSERT INTO users (user_id, email, password, name, last_name, age, user_type) 
VALUES
    ('b33bc0d9-fd68-4723-953d-2812894257ca', 'aelo@gmail.com', 'admin1234', 'Angel', 'Lugo', 25, 'ADMINISTRATOR'),
    ('5e3ee61a-57ab-49a3-91c5-c76ea7e9ea87', 'admin@gmail.com', 'admin1234', 'admin', 'admin', 100, 'ADMINISTRATOR');

-- LOAD DATAS
INSERT INTO movies (movie_id, title, release_year, genre, price)
VALUES
    ('bea4d863-ca64-445d-befd-e9697920d3aa', 'The Shaw shank Redemption', 1994, 'HORROR', 15.99),
    ('f22b9187-79e0-41ed-b359-73cd7606a87e', 'Ant Man', 2019, 'ADVENTURE', 15.00),
    ('18cd532f-968d-4300-9d5d-24fe5acc9599', 'Fallen', 1996, 'HORROR', 23.99),
    ('51e3394a-1279-4a9c-aee6-0ef0801f7d88', 'The barbershop', 2006, 'COMEDY', 6.50),
    ('bd5fdfa8-681f-4806-b84b-96be227e7048', 'The last dance', 2021, 'SPORTS', 55.99),
    ('040396f0-2932-4a88-962e-3cbc41db9637', 'Peter Pan', 2004, 'ADVENTURE', 15.99),
    ('64dcbc95-0083-42a9-8503-496fe737464a', 'Fast & Furious 7', 2018, 'ACTION', 36.00),
    ('760dd4c3-27c0-4c27-bdcd-945a79419a8b', 'Harry Potter', 2000, 'ACTION', 26.50),
    ('34d4c4fc-bb3b-4eef-9254-fe4c251be3c8', 'Jungle book', 2004, 'ADVENTURE', 25.00);