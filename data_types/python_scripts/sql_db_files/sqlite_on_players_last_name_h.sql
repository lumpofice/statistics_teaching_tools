--1) Create 'colleges' table
CREATE TABLE colleges
(
college_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
college_name TEXT CHECK(LENGTH(college_name)<=100)
);

--2) Fill 'colleges' table
INSERT INTO colleges (college_name)
SELECT
DISTINCT colleges 
FROM
players_last_name_h;

--3) Create 'positions' table
CREATE TABLE positions
(
position_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
position_name TEXT CHECK(LENGTH(position_name)<=10)
);

--4) Fill 'positions' table
INSERT INTO positions (position_name)
SELECT
DISTINCT pos
FROM
players_last_name_h;

--5) Create 'players_last_names_h' table
CREATE TABLE players_last_names_h
(
player_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
player_name TEXT CHECK(LENGTH(player_name)<=100),
from_year INTEGER,
to_year INTEGER,
position_id INTEGER NOT NULL,
height TEXT,
weight INTEGER,
birth_date TEXT,
college_id INTEGER NOT NULL,
FOREIGN KEY (position_id) REFERENCES positions (position_id),
FOREIGN KEY (college_id) REFERENCES colleges (college_id)
);

--6) Fill 'players_last_names_h' table

--i) Create 'positions_bridge' temp table
CREATE TEMP TABLE positions_bridge AS
SELECT
ph.player_id AS player_id,
ph.pos AS position_name,
p.position_id AS position_id
FROM
players_last_name_h AS ph
LEFT JOIN
positions AS p
ON
ph.pos = p.position_name;

--ii) Create 'colleges_bridge' temp table
CREATE TEMP TABLE colleges_bridge AS
SELECT
ph.player_id AS player_id,
ph.colleges AS colleges,
c.college_id AS college_id
FROM
players_last_name_h AS ph
LEFT JOIN
colleges AS c
ON
ph.colleges = c.college_name;

--iii) Disable foreign key checks
PRAGMA foreign_keys=0;

--iv) Fill table
INSERT INTO players_last_names_h 
(player_id, player_name, from_year, to_year, position_id,
height, weight, birth_date, college_id)
SELECT
ph.player_id AS player_id,
ph.player AS player_name,
ph.from_year AS from_year,
ph.to_year AS to_year,
pb.position_id AS position_id,
ph.ht AS height,
ph.wt AS weight,
ph.birth_date AS birth_date,
cb.college_id AS college_id
FROM 
players_last_name_h AS ph
INNER JOIN
positions_bridge AS pb
ON 
ph.player_id = pb.player_id
INNER JOIN
colleges_bridge AS cb
ON
ph.player_id = cb.player_id;

--v) Enable foreign key checks
PRAGMA foreign_keys=1;

--7) Drop initial 'players_last_name_h' table
DROP TABLE players_last_name_h; 

--8) Rename 'players_last_names_h' table to 'players_last_name_h'
ALTER TABLE players_last_names_h
RENAME TO players_last_name_h;
