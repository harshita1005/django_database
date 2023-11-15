show databases;
create database test;
use test;

CREATE TABLE data(Id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
summary_file_name varchar(255),
date DATE,
time TIME,
current_status varchar(20),
test_name varchar(255),
log_file varchar(255),
html_report varchar(255),
video_file varchar(255));

show tables;
SELECT * FROM data;

SELECT test_name from data;

DROP TABLE data;

DROP database test;