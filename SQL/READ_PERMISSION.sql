USE BESANT;
SELECT * FROM EMPLOYEE;

UPDATE EMPLOYEE SET EMP_SALARY = 90000 WHERE EMP_ID = 1;

/* Error Code: 1142. UPDATE command denied to user 'dummy'@'localhost' for table 'employee' */