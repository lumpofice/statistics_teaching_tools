--1) Create 'player_points_rankings_21_22' table
CREATE TABLE player_points_rankings_21_22
(
ranking INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
player_name TEXT CHECK(LENGTH(player_name)<=50),
points INTEGER NOT NULL
);

--2) Fill 'player_points_rankings_21_22' table
INSERT INTO player_points_rankings_21_22
SELECT
*
FROM
players_points_rankings_21_22;

--3) Drop 'players_points_rankings_21_22' table
DROP TABLE players_points_rankings_21_22;

--4) Rename 'player_points_rankings_21_22' table to 
--players_points_rankings_21_22
ALTER TABLE player_points_rankings_21_22
RENAME TO players_points_rankings_21_22;
