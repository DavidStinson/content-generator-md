CREATE TABLE capstone (
  ID SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50)
);

INSERT INTO capstone (first_name, last_name) VALUES ('Marc', 'Wright'), ('Ben', 'Piper'), ('Troy', 'Swayzee');
