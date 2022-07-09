--1) Create the 'the_season_09_10' table
CREATE TABLE the_season_09_10
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--2) Fill 'the_season_09_10' table
INSERT INTO the_season_09_10
SELECT
*
FROM
season_09_10;

--3) Drop 'season_09_10' table
DROP TABLE season_09_10;

--4) Rename 'the_season_09_10' table to 'season_09_10'
ALTER TABLE the_season_09_10
RENAME TO season_09_10;


--5) Create the 'the_season_10_11' table
CREATE TABLE the_season_10_11
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--6) Fill 'the_season_10_11' table
INSERT INTO the_season_10_11
SELECT
*
FROM
season_10_11;

--7) Drop 'season_10_11' table
DROP TABLE season_10_11;

--8) Rename 'the_season_10_11' table to 'season_10_11'
ALTER TABLE the_season_10_11
RENAME TO season_10_11;


--9) Create the 'the_season_11_12' table
CREATE TABLE the_season_11_12
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--10) Fill 'the_season_11_12' table
INSERT INTO the_season_11_12
SELECT
*
FROM
season_11_12;

--11) Drop 'season_11_12' table
DROP TABLE season_11_12;

--12) Rename 'the_season_11_12' table to 'season_11_12'
ALTER TABLE the_season_11_12
RENAME TO season_11_12;


--13) Create the 'the_season_12_13' table
CREATE TABLE the_season_12_13
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--14) Fill 'the_season_12_13' table
INSERT INTO the_season_12_13
SELECT
*
FROM
season_12_13;

--15) Drop 'season_12_13' table
DROP TABLE season_12_13;

--16) Rename 'the_season_12_13' table to 'season_12_13'
ALTER TABLE the_season_12_13
RENAME TO season_12_13;


--17) Create the 'the_season_13_14' table
CREATE TABLE the_season_13_14
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--18) Fill 'the_season_13_14' table
INSERT INTO the_season_13_14
SELECT
*
FROM
season_13_14;

--19) Drop 'season_13_14' table
DROP TABLE season_13_14;

--20) Rename 'the_season_13_14' table to 'season_13_14'
ALTER TABLE the_season_13_14
RENAME TO season_13_14;


--21) Create the 'the_season_14_15' table
CREATE TABLE the_season_14_15
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--22) Fill 'the_season_14_15' table
INSERT INTO the_season_14_15
SELECT
*
FROM
season_14_15;

--23) Drop 'season_14_15' table
DROP TABLE season_14_15;

--24) Rename 'the_season_14_15' table to 'season_14_15'
ALTER TABLE the_season_14_15
RENAME TO season_14_15;


--25) Create the 'the_season_15_16' table
CREATE TABLE the_season_15_16
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--26) Fill 'the_season_15_16' table
INSERT INTO the_season_15_16
SELECT
*
FROM
season_15_16;

--27) Drop 'season_15_16' table
DROP TABLE season_15_16;

--28) Rename 'the_season_15_16' table to 'season_15_16'
ALTER TABLE the_season_15_16
RENAME TO season_15_16;


--29) Create the 'the_season_16_17' table
CREATE TABLE the_season_16_17
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--30) Fill 'the_season_16_17' table
INSERT INTO the_season_16_17
SELECT
*
FROM
season_16_17;

--31) Drop 'season_16_17' table
DROP TABLE season_16_17;

--32) Rename 'the_season_16_17' table to 'season_16_17'
ALTER TABLE the_season_16_17
RENAME TO season_16_17;


--33) Create the 'the_season_17_18' table
CREATE TABLE the_season_17_18
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--34) Fill 'the_season_17_18' table
INSERT INTO the_season_17_18
SELECT
*
FROM
season_17_18;

--35) Drop 'season_17_18' table
DROP TABLE season_17_18;

--36) Rename 'the_season_17_18' table to 'season_17_18'
ALTER TABLE the_season_17_18
RENAME TO season_17_18;


--37) Create the 'the_season_18_19' table
CREATE TABLE the_season_18_19
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--38) Fill 'the_season_18_19' table
INSERT INTO the_season_18_19
SELECT
*
FROM
season_18_19;

--39) Drop 'season_18_19' table
DROP TABLE season_18_19;

--40) Rename 'the_season_18_19' table to 'season_18_19'
ALTER TABLE the_season_18_19
RENAME TO season_18_19;


--41) Create the 'the_season_19_20' table
CREATE TABLE the_season_19_20
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--42) Fill 'the_season_19_20' table
INSERT INTO the_season_19_20
SELECT
*
FROM
season_19_20;

--43) Drop 'season_19_20' table
DROP TABLE season_19_20;

--44) Rename 'the_season_19_20' table to 'season_19_20'
ALTER TABLE the_season_19_20
RENAME TO season_19_20;


--45) Create the 'the_season_20_21' table
CREATE TABLE the_season_20_21
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--46) Fill 'the_season_20_21' table
INSERT INTO the_season_20_21
SELECT
*
FROM
season_20_21;

--47) Drop 'season_20_21' table
DROP TABLE season_20_21;

--48) Rename 'the_season_20_21' table to 'season_20_21'
ALTER TABLE the_season_20_21
RENAME TO season_20_21;


--49) Create the 'the_season_21_22' table
CREATE TABLE the_season_21_22
(
game_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
game_date TEXT,
age TEXT,
opponent TEXT,
outcome TEXT,
started INTEGER,
field_goals INTEGER,
field_goal_attempts INTEGER,
field_goal_pct REAL,
three_points INTEGER,
three_point_attempts INTEGER,
three_point_pct REAL,
free_throw INTEGER,
free_throw_attempts INTEGER,
free_throw_pct REAL,
offense_rebound INTEGER,
defense_rebound INTEGER,
total_rebound INTEGER,
assists INTEGER,
steals INTEGER,
blocks INTEGER,
turnovers INTEGER,
personal_fouls INTEGER,
points INTEGER,
game_score REAL,
plus_minus INTEGER,
away_game INTEGER
);

--50) Fill 'the_season_21_22' table
INSERT INTO the_season_21_22
SELECT
*
FROM
season_21_22;

--51) Drop 'season_21_22' table
DROP TABLE season_21_22;

--52) Rename 'the_season_21_22' table to 'season_21_22'
ALTER TABLE the_season_21_22
RENAME TO season_21_22;
