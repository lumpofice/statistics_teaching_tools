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
fall_2008 INTEGER,
fall_2009 INTEGER,
fall_2010 INTEGER,
fall_2011 INTEGER,
fall_2012 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

--4) Create 'graduate' table
CREATE TABLE graduate
(
ethnic_origin_id INTEGER NOT NULL,
fall_2008 INTEGER,
fall_2009 INTEGER,
fall_2010 INTEGER,
fall_2011 INTEGER,
fall_2012 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

--5) Create 'combined' table
CREATE TABLE combined
(
ethnic_origin_id INTEGER NOT NULL,
fall_2008 INTEGER,
fall_2009 INTEGER,
fall_2010 INTEGER,
fall_2011 INTEGER,
fall_2012 INTEGER,
FOREIGN KEY (ethnic_origin_id) 
REFERENCES ethnic_origin (ethnic_origin_id)
);

PRAGMA foregin_keys=0;

--6) Fill 'undergraduate' table
INSERT INTO undergraduate
SELECT 
eo.ethnic_origin_id AS ethnic_origin_id,
su.fall_2008 AS fall_2008,
su.fall_2009 AS fall_2009,
su.fall_2010 AS fall_2010,
su.fall_2011 AS fall_2011,
su.fall_2012 AS fall_2012
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
sg.fall_2008 AS fall_2008,
sg.fall_2009 AS fall_2009,
sg.fall_2010 AS fall_2010,
sg.fall_2011 AS fall_2011,
sg.fall_2012 AS fall_2012
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
sc.fall_2008 AS fall_2008,
sc.fall_2009 AS fall_2009,
sc.fall_2010 AS fall_2010,
sc.fall_2011 AS fall_2011,
sc.fall_2012 AS fall_2012
FROM 
ethnic_origin AS eo
INNER JOIN 
source_combined AS sc
ON
eo.ethnic_origin_name = sc.student_ethnic_origin;

PRAGMA foreign_keys=1;

