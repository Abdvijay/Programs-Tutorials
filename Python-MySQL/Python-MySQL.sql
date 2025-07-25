show databases;

create database python_mysql;

use python_mysql;


show tables;

create table student(
name varchar(50) not null,
college varchar(50) not null);

select * from student;