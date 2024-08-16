use hr;
-- SELECT(DQL)
select * from cars;

SELECT * FROM EMPLOYEES;

SELECT EMPLOYEE_ID, FIRST_NAME, SALARY FROM EMPLOYEES;

select FIRST_NAME from employees;

select department_id from employees;
-- DISTINCT
select distinct department_id,MANAGER_ID from employees;

-- WHERE CLAUSE(OPERATORS)
select * from employees where salary=10000;

select * from employees where salary>10000;

select employee_id , first_name, department_id,salary,JOB_ID from employees where job_id!='IT_Prog';

select * from employees where salary BETWEEN 10000 and 15000;

select * from employees 
where salary>10000 AND job_id='ac_mgr'; 

select * from employees
where manager_id>101 OR salary=10000;

select  * from countries
where NOT country_name= 'Argentina';

select * from jobs
where  NOT min_salary=4000 AND NOT max_salary<10000; 

select * from countries
where country_name='China' AND (region_id=2 OR region_id=3);

-- ORDER BY

select * from employees
order by salary;

select * from employees
order by first_name DESC;

select * from employees
order by salary,JOB_ID;

select * from countries
order by region_id desc,country_name asc ;

select * from employees 
where department_id=100 order by salary,first_name;

select * from employees
order by hire_date;

-- IS NULL/NOT

select first_name, last_name,email,MANAGER_ID
from employees
where manager_id IS null;

select first_name,job_id,phone_number,commission_pct
from employees
where commission_pct IS NOT NULL;

-- LIMIT

select * from employees
limit 5;

select * from employees
where department_id=60
limit 3;

-- MIN&MAX

select max(salary) as 'largest salary'
from employees;

select min(commission_pct) as minimum_commission
from employees;

-- COUNT,AVG & SUM

select count(model) from cars;

select avg(salary) as AVERAGE_SALARY
from employees
where job_id = 'st_clerk'; 

select sum(salary) from employees;

-- LIKE & NOT LIKE

select * from employees
where first_name like 'a%';

select * from employees
where first_name not like 'a%';

select * from cars
where BRAND like '%ki';

select * from cars
where BRAND NOT like '%ki';

select * from countries
where country_name like '%ni%';

select * from countries
where country_name NOT like '%ni%';

select * from cars
where MODEL like '%__ga';

select * from cars
where MODEL NOT like '%__ga';
 
select * from cars
where BRAND like '%_ata';

select * from cars
where BRAND NOT like '%_ata';

-- 	DDL (CREATE, ALTER, TRUNCATE, DROP)

-- create database my_data;
use my_data;

DROP TABLE IF EXISTS PERSON;
create table person  
(person_id int, first_name varchar (150), last_name varchar(150), phone_number varchar(12));

-- drop database testdb;

alter table person 
add column email varchar(150);

alter table person
modify column phone_number int;

alter table person
drop column email;

select * from person;

drop table person;

-- DML(INSERT INTO, UPDATE, DELETE)

create table person  
(person_id int, first_name varchar (150), last_name varchar(150), phone_number varchar(12));

SELECT * FROM person;

INSERT INTO PERSON VALUES
(101, 'JOHN','MATHEW',987654321);

INSERT INTO PERSON VALUES
(102,'VIRAT','KOHLI',76578954),
(103,'TIM','DAVID',8762345);

INSERT INTO PERSON (PERSON_ID,FIRST_NAME) VALUES
(104,'BABAR');

SELECT * FROM person;


UPDATE PERSON
SET LAST_NAME = 'ASSAM', PHONE_NUMBER = 1234567895
WHERE PERSON_ID = 104;

SELECT * FROM PERSON;

DELETE FROM person
WHERE PERSON_ID = 102;

-- TRUNCATE TABLE PERSON;

use  my_data;
DROP  TABLE IF EXISTS JOB;
create table job
(employee_id int,employee_name varchar(100),job_name varchar(100),manager_id int ,salary int);
insert into job values
(100,'Sam','Accountant',3590,20000);
select * from job;
insert into job values
(101,'Michael','Teacher',3595,15000),
(102,"Peter",'Business',3598,23000);
insert into job(employee_id,employee_name) values
(103,'Maya');
update job
set job_name='Doctor',manager_id=3600,salary=24000
where employee_id=103;
delete from job
where employee_id=101;
select * from job;
-- TRUNCATE TABLE JOB;


-- CONSTRAINTS (NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT, CREATE INDEX, AUTO INCREMENT)

USE MY_DATA;

-- NOT NULL
DROP TABLE IF exists SCHOOL;
create table school
(student_id int,student_name varchar(200)not null,age int not null,class int);

SELECT * FROM SCHOOL;
insert into school values
(001,'Rohit',14,8);
insert into school values
(002,'Manu',12,6),
(104,'Anu',16,10);
INSERT INTO SCHOOL VALUES
(105,'REETA',14,8);
SELECT * FROM SCHOOL;
DELETE  FROM SCHOOL
WHERE STUDENT_ID=100;

-- UNIQUE

ALTER TABLE SCHOOL
ADD UNIQUE(STUDENT_ID);
ALTER TABLE school
ADD CONSTRAINT UC_SCHOOL
UNIQUE(STUDENT_ID,STUDENT_NAME);
ALTER TABLE SCHOOL
DROP INDEX UC_SCHOOL;

-- PRIMARY KEY

DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE
(ID INT NOT NULL, LAST_NAME VARCHAR(100) NOT NULL, FIRST_NAME VARCHAR(100), AGE INT);
SELECT * FROM EMPLOYEE;
ALTER TABLE EMPLOYEE
ADD PRIMARY KEY(ID);
ALTER TABLE employee
DROP PRIMARY KEY;

ALTER TABLE employee
ADD CONSTRAINT E_EMPLOYEE primary key
(ID,LAST_NAME);

SELECT TABLE_NAME,CONSTRAINT_NAME,CONSTRAINT_TYPE FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='EMPLOYEE';

INSERT INTO EMPLOYEE VALUES
(100,'ALI','MUHAMMED',24),
(105,'MARY','AKSA',21),
(103,'MARYAM','AYSHA',20);

SELECT * FROM EMPLOYEE;

-- FOREIGN KEY

DROP table if exists ORDERS;
CREATE TABLE ORDERS
(ORDER_ID INT NOT NULL, ORDER_NUMBER INT NOT NULL,EMP_ID INT,
PRIMARY KEY (ORDER_ID),
foreign key (EMP_ID) REFERENCES EMPLOYEE(ID));

select * from ORDERS;

INSERT INTO ORDERS values
(2001,23445,103),
(2006,54675,105);
INSERT INTO ORDERS VALUES
( 2004,67476,110);

-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`my_data`.`orders`, CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`EMP_ID`) REFERENCES `employee` (`ID`))

USE MY_DATA;
SELECT *  FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME='ORDERS'AND CONSTRAINT_SCHEMA= 'MY_DATA';

-- CHECK

ALTER TABLE EMPLOYEE
ADD CHECK(AGE>=18 AND ID<106);
ALTER TABLE employee
DROP CONSTRAINT EMPLOYEE_CHK_1;

INSERT INTO EMPLOYEE values
(106,'SEBASTIAN','MARY',17,'KANNUR');

-- DEFAULT

select * FROM EMPLOYEE;

ALTER TABLE employee
ADD COLUMN CITY VARCHAR(90);

ALTER TABLE EMPLOYEE
ALTER CITY SET DEFAULT 'DELHI';

INSERT INTO EMPLOYEE (ID,LAST_NAME,FIRST_NAME,AGE)VALUES
(102,'MEHRIN','ASIYA',19),
(104,'RAMESH','RIYA',23);


select * FROM EMPLOYEE;

ALTER TABLE EMPLOYEE
ALTER CITY DROP DEFAULT;
INSERT INTO EMPLOYEE(ID,LAST_NAME,FIRST_NAME,AGE)VALUES
(101,'SINGH','RANITH',32);

DROP TABLE IF EXISTS MOVIES;
CREATE TABLE MOVIES
(MOVIE_ID INT AUTO_INCREMENT,MOVIE_NAME VARCHAR(90),LANGUAGE VARCHAR (90) ,YEAR INT,
PRIMARY KEY(MOVIE_ID)); 

INSERT INTO MOVIES(MOVIE_NAME,YEAR) VALUES 
('TURBO',2024),
('PREMALU',2024);
select* FROM MOVIES;

CREATE INDEX idx_movie
on movies (movie_name,MOVIE_ID);

ALTER TABLE MOVIES
DROP INDEX IDX_MOVIE;

alter table movies
auto_increment=100;

insert into movies
(movie_name,language)
values('AVESHAM','MALAYALAM');

select * from orders;
select * from orders where order_date=current_date;

select * from employee;

update employee
set city='AGRA' where ID=100 ;

update employee
SET CITY='BRAZIL' WHERE ID=103;
update employee
SET CITY='DELHI' WHERE ID=105;
 
 
 CREATE VIEW  DELHI_EMPLOYEES AS
 SELECT FIRST_NAME,LAST_NAME FROM EMPLOYEE
 WHERE CITY='DELHI';
 
 SELECT * FROM DELHI_EMPLOYEES;
 
 
 CREATE view EMPLOYEE_ABOVE_AVERAGE_AGE AS
 SELECT FIRST_NAME,AGE FROM EMPLOYEE
 WHERE AGE>(SELECT AVG(AGE) FROM EMPLOYEE);
 
 SELECT * FROM employee_above_average_age;
 
use hr; 
 
 select * from EMPLOYEES;
 
CREATE VIEW JOB_ABOVE_AVERAGE_SALARY AS 
SELECT FIRST_NAME,JOB_ID,SALARY FROM EMPLOYEES
WHERE SALARY>(SELECT AVG(SALARY) FROM EMPLOYEES);

SELECT * FROM JOB_ABOVE_AVERAGE_SALARY;
 
 USE HR;
 SELECT * FROM PERSON;
 SELECT * FROM ORDERS;
 SELECT * FROM COUNTRIES;
 
 select * FROM EMPLOYEES;
 SELECT * FROM JOB_HISTORY;
 
 SELECT EMPLOYEES.JOB_ID,EMPLOYEES.FIRST_NAME,JOB_HISTORY.DEPARTMENT_ID
 FROM EMPLOYEES
 INNER JOIN JOB_HISTORY ON EMPLOYEES.EMPLOYEE_ID=JOB_HISTORY.EMPLOYEE_ID;
 
 
SELECT EMPLOYEES.JOB_ID,EMPLOYEES.FIRST_NAME,JOB_HISTORY.DEPARTMENT_ID
 FROM EMPLOYEES
 LEFT JOIN JOB_HISTORY ON EMPLOYEES.EMPLOYEE_ID=JOB_HISTORY.EMPLOYEE_ID;

SELECT E.JOB_ID,E.FIRST_NAME,J.DEPARTMENT_ID
FROM EMPLOYEES E
RIGHT JOIN JOB_HISTORY J ON E.EMPLOYEE_ID=J.EMPLOYEE_ID;

USE MY_DATA;
DROP TABLE IF EXISTS CLASS;
CREATE TABLE CLASS(
ID INT UNSIGNED PRIMARY KEY,
F_NAME VARCHAR(10)
);

INSERT INTO CLASS VALUES
(101,'AKASH'),
(102,'AMAL'),
(103,'ANAGHA');

SELECT * FROM CLASS;
USE HR;
select *  from employees;

select employee_id,manager_id,DEPARTMENT_ID from employees;

SELECT DEPARTMENT_ID,COUNT(EMPLOYEE_ID) AS EMPLOYEE_COUNT
FROM EMPLOYEES  
GROUP BY DEPARTMENT_ID;


SELECT D.FIRST_NAME,E.DEPARTMENT_ID, COUNT(E.EMPLOYEE_ID) AS EMPLOYEE_COUNT
FROM EMPLOYEES E 
INNER JOIN EMPLOYEES D ON E.MANAGER_ID = D.EMPLOYEE_ID
GROUP BY E.DEPARTMENT_ID,E.MANAGER_ID;

SELECT e.first_name, 
       e.manager_id, 
       COUNT(ed.employee_id) AS num_employees_in_department
FROM Employees e
JOIN Employees ed ON e.department_id = ed.department_id
GROUP BY e.first_name, e.manager_id
ORDER BY e.first_name;





SELECT COUNT(EMPLOYEE_ID) FROM EMPLOYEES 
WHERE FIRST_NAME='ALEXANDER';

SELECT MAX(SALARY)
FROM EMPLOYEES
WHERE SALARY<(SELECT MAX(SALARY) FROM EMPLOYEES);
USE HR;
SELECT first_NAME, SALARY FROM EMPLOYEES
order by SALARY desc LIMIT 1 OFFSET 1;
