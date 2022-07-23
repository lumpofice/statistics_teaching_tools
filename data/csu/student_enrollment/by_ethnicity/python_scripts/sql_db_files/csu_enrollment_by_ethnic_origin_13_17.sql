--1) Create 'ethnic_origin' table
CREATE TABLE ethnic_origin
(
ethnic_origin_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
ethnic_origin_name TEXT
);

--2) Fill 'ethnic_origin' table
INSERT INTO ethnic_origin (ethnic_origin_name)
SELECT
student_ethnic_origin
FROM
source_combined;

--3) Create 'undergraduate' table
CREATE TABLE undergraduate
(
ethnic_origin_id INTEGER NOT NULL,
fall_2013 INTEGER,
fall_2014 INTEGER,
fall_2015 INTEGER,
fall_2016 INTEGER,
fall_2017 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

--4) Create 'graduate' table
CREATE TABLE graduate
(
ethnic_origin_id INTEGER NOT NULL,
fall_2013 INTEGER,
fall_2014 INTEGER,
fall_2015 INTEGER,
fall_2016 INTEGER,
fall_2017 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

--5) Create 'combined' table
CREATE TABLE combined
(
ethnic_origin_id INTEGER NOT NULL,
fall_2013 INTEGER,
fall_2014 INTEGER,
fall_2015 INTEGER,
fall_2016 INTEGER,
fall_2017 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

PRAGMA foregin_keys=0;

--6) Fill 'undergraduate' table
INSERT INTO undergraduate
SELECT 
eo.ethnic_origin_id AS ethnic_origin_id,
su.fall_2013 AS fall_2013,
su.fall_2014 AS fall_2014,
su.fall_2015 AS fall_2015,
su.fall_2016 AS fall_2016,
su.fall_2017 AS fall_2017
FROM 
ethnic_origin AS eo
INNER JOIN 
source_undergraduate AS su
ON
eo.ethnic_origin_name = su.student_ethnic_origin;

--7) Fill 'graduate' table
INSERT INTO graduate
SELECT 
eo.ethnic_origin_id AS ethnic_origin_id,
sg.fall_2013 AS fall_2013,
sg.fall_2014 AS fall_2014,
sg.fall_2015 AS fall_2015,
sg.fall_2016 AS fall_2016,
sg.fall_2017 AS fall_2017
FROM 
ethnic_origin AS eo
INNER JOIN 
source_graduate AS sg
ON
eo.ethnic_origin_name = sg.student_ethnic_origin;

--8) Fill 'undergraduate' table
INSERT INTO combined
SELECT 
eo.ethnic_origin_id AS ethnic_origin_id,
sc.fall_2013 AS fall_2013,
sc.fall_2014 AS fall_2014,
sc.fall_2015 AS fall_2015,
sc.fall_2016 AS fall_2016,
sc.fall_2017 AS fall_2017
FROM 
ethnic_origin AS eo
INNER JOIN 
source_combined AS sc
ON
eo.ethnic_origin_name = sc.student_ethnic_origin;

PRAGMA foreign_keys=1;


