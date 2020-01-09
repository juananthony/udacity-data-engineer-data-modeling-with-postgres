# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time bigint, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name varchar NOT NULL, last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar NOT NULL, artist_id varchar NOT NULL, year int, duration numeric(10,5));
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, latitude float8, longitude float8);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time time PRIMARY KEY, hour int, day int, week int, month int, year int , weekday int);
""")

# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE
    SET first_name = excluded.first_name,
        last_name = excluded.last_name,
        gender = excluded.gender,
        level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title , artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO UPDATE
    SET title = excluded.title,
        artist_id = excluded.title,
        year = excluded.year,
        duration = excluded.duration
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO UPDATE 
    SET name = excluded.name,
        location = excluded.location,
        latitude = excluded.latitude,
        longitude = excluded.longitude
""")

time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO UPDATE
    SET hour = excluded.hour,
        day = excluded.day,
        week = excluded.week,
        month = excluded.month,
        year = excluded.year,
        weekday = excluded.weekday
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id 
FROM songs s
INNER JOIN artists a ON a.artist_id = s.artist_id
WHERE s.title LIKE %s AND a.name LIKE %s AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]