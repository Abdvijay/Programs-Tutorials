# -------------------------------- VIEWS -----------------------------------------------------

CREATE TABLE employees (
employee_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
hire_date DATE,
job_title VARCHAR(50),
salary DECIMAL (10, 2)
);

INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_title, salary)
VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '2022-05-01', 'Software Engineer', 85000.00),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '2023-03-15', 'Data Scientist', 92000.00),
( 3, 'Alice', 'Johnson', 'alice.johnson@example.com', '2024-05-01', 'Engineer', 95000.00),
( 4, 'Mark', 'Taylor', 'mark.taylor@example.com', '2022-11-15', 'Manager', 100000.00),
(5, 'Gowtham', 'sb', 'mark.taylor@example.com', '2022-11-15', 'Data Engineer', 100000.00),
(6, 'Peter', 'sb', 'mark.taylor@example.com', '2022-11-15', 'Data Engineer', 120000.00);

SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME,SALARY FROM EMPLOYEES WHERE SALARY >= 90000;

2	Jane	Smith	92000.00
3	Alice	Johnson	95000.00
4	Mark	Taylor	100000.00
5	Gowtham	sb	    100000.00
6	Peter	sb	    120000.00

CREATE VIEW HIGH_EARNERS AS (SELECT EMPLOYEE_ID,FIRST_NAME,LAST_NAME,SALARY FROM EMPLOYEES WHERE SALARY >= 90000);

SELECT * FROM HIGH_EARNERS;

2	Jane	Smith	92000.00
3	Alice	Johnson	95000.00
4	Mark	Taylor	100000.00
5	Gowtham	sb	    100000.00
6	Peter	sb	    120000.00

INSERT INTO employees
VALUES (7, 'john', 'sb', 'mark.taylor@example.com', '2022-11-15', 'Data Engineer',120000.00);

SELECT * FROM HIGH_EARNERS;

2	Jane	Smith	92000.00
3	Alice	Johnson	95000.00
4	Mark	Taylor	100000.00
5	Gowtham	sb	    100000.00
6	Peter	sb	    120000.00
7	john	sb	    120000.00

TRUNCATE TABLE EMPLOYEES;
DROP VIEW HIGH_EARNERS;

POINTS TO REMEMBER :

    1. VIEWS IS SIMPLY LOOK LIKE TABLE BUT IT DOES NOT STORE IN STORAGE.
    2. MAIN ADVANTAGE IS SECURITY BECAUSE WE DOES NOT DISPLAY THE HIGH_EARNERS LOGIC QUERIES WE JUST SHOW HIGH_EARNERS.
    3. ANOTHER ADVANTAGE IS IF WE A NEW ROW THEN THE HIGH_EARNERS ALWAYS FETCH IT AND UPDATED IT WE DONT RUN ABOVE EMPLOYEES MANAUALLY.