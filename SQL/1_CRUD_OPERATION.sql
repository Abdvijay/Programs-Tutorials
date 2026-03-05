1. #INSTALLATION MYSQL TO YOUR SYSTEM :

    1. Go to https://dev.mysql.com/downloads/installer/ to downloads the MYSQL installer.
    2. Setup MYSQL within your system.
    3. Check MYSQL WORKBENCH is installed or not.
    4. Make your connection with MYSQL WORKBENCH and start working on it.

2. #CHECK YOUR DATABASES : 

    1. SHOW DATABASES;
    2. It displays all the existing DATABASES NAMES

3. #CREATE DATABASES : 

    1. CREATE DATABASE DATABASE_NAME; (eg : CREATE DATABASE VIJAY_SQL;)
    2. Before creating TABLE we need to choose DATABASE.

4. #CHOOSE DATABASES :

    1. USE DATABASE_NAME; (eg : USE VIJAY_SQL;)
    2. Then you can insert more tables into this DATABASE.
    3. SHOW TABLES; (It displays all tables name under selected DATABASE)

5. #CRUD OPERATION : 

    1. CREATE TABLE : 
        CREATE TABLE TABLE_NAME(
            FIELDS DATA_TYPES CONSTRAINTS,
            ....
        );
        
        CREATE TABLE VIJAY_TEST_TABLE(
            SNO INT,
            SNAME VARCHAR(100)
        );

    2. READ -> SELECT :
        SELECT * FROM TABLE_NAME;
                OR
        SELECT FIELDS_NAME FROM TABLE_NAME;

        SELECT * FROM VIJAY_TEST_TABLE; ( It returns all the fields from specified table)
        SELECT SNO,SNAME FROM VIJAY_TEST_TABLE; (It returns only the specified fields from specified table)

    3. UPDATE TABLE :
        UPDATE TABLE_NAME
        SET FIELDS_NAME = NEW_VALUE
        WHERE FIELDS_NAME = VALUE;

        UPDATE VIJAY_TEST_TABLE
        SET SNAME = "DEEKSHA"
        WHERE SNO = 100;

    4. DELETE TABLE :
        DELETE FROM TABLE_NAME
        WHERE FIELDS_NAME = VALUE;

        DELETE FROM VIJAY_TEST_TABLE
        WHERE SNO = 100;

6. #TRUNCATE TABLE : (It will erase all the DATA from the TABLE not delete the SCHEMA)

    TRUNCATE TABLE TABLE_NAME;

    TRUNCATE TABLE VIJAY_TEST_TABLE;

7. #DROP TABLE : (It will DELETE all the data from the TABLE and DELETE the SCHEMA also)

    DROP TABLE TABLE_NAME;

    DROP TABLE VIJAY_TEST_TABLE;