-- CREATE DATABASE bmat; # is already created by postgres docker init script, using env
-- CREATE USER app_user WITH ENCRYPTED PASSWORD '123';
-- GRANT ALL PRIVILEGES ON DATABASE bmat TO app_user;
CREATE TABLE IF NOT EXISTS works_metadata
(title text,
contributors text,
iswc text);
