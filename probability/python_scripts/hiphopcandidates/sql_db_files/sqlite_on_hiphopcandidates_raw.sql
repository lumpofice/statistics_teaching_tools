--1) Create 'artists' table
CREATE TABLE artists
(
artist_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
artist_name TEXT CHECK( LENGTH(artist_name) <= 50 )
);

--2) Fill 'artists' table
INSERT INTO artists (artist_name)
SELECT
DISTINCT artist
FROM
rapper_candidate_map;

--3) Create 'candidates' table
CREATE TABLE candidates
(
candidate_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
candidate_name TEXT CHECK( LENGTH(candidate_name) <= 50 )
);

--4) Fill 'candidates' table
INSERT INTO candidates (candidate_name)
SELECT
DISTINCT candidate
FROM
rapper_candidate_map;

--5) Create table 'song_entries' table
CREATE TABLE song_entries
(
entry_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
song TEXT,
artist_id INTEGER NOT NULL,
candidate_id INTEGER NOT NULL,
sentiment TEXT CHECK( sentiment IN ('positive','negative','neutral') ),
theme TEXT,
album_release_year TEXT,
FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
FOREIGN KEY (candidate_id) REFERENCES candidates (candidate_id)
);

--6) Fill 'song_entries' table

--i) Create 'artists_bridge' temp table
CREATE TEMP TABLE artists_bridge AS
SELECT
rcm.id AS id,
rcm.artist AS artist,
art.artist_id AS artist_id
FROM
rapper_candidate_map AS rcm
LEFT JOIN
artists AS art
ON
rcm.artist = art.artist_name;

--ii) Create 'candidates_bridge' temp table
CREATE TEMP TABLE candidates_bridge AS
SELECT
rcm.id AS id,
rcm.candidate AS candidate,
cand.candidate_id AS candidate_id
FROM
rapper_candidate_map AS rcm
LEFT JOIN
candidates AS cand
ON
rcm.candidate = cand.candidate_name;

--iii) Disable foreign key checks
PRAGMA foreign_keys=0;

--iv) Fill table
INSERT INTO song_entries 
(entry_id, song, artist_id, candidate_id, sentiment, theme,
album_release_year)
SELECT
rcm.id AS entry_id,
rcm.song AS song,
artb.artist_id AS artist_id,
candb.candidate_id AS candidate_id,
rcm.sentiment AS sentiment,
rcm.theme AS theme,
rcm.album_release_date AS album_release_year
FROM
rapper_candidate_map AS rcm
INNER JOIN
artists_bridge AS artb
ON 
rcm.id = artb.id
INNER JOIN
candidates_bridge AS candb
ON
rcm.id = candb.id;

--v) Enable foreign key checks
PRAGMA foreign_keys=1;

--7) Drop the initial 'rapper_candidate_map' table 
DROP TABLE rapper_candidate_map;

