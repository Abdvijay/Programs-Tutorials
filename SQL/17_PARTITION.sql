# -------------------------------RANGE PARTITION ----------------------------------------

POINTS TO REMEMBER :

    1. PARTITION IS JUST SEPARATING DATA AND INCREASE PERFORMANCE WHILE FETCHING THE DATA JUST LIKE LAPTOP DISK PARTITION.
    2. IF C DISK HAS SYSTEM_FILES AND EDUCATION RELATED FILES BUT D DISK HAS ENTERTAINMENT PURPOSE.
    3. IF U MOVE THE NEW MOVIE TO YOUR LAPTOP FIRST COMES INTO YOUR MIND IS D DISK INSTEAD OF C DISK.
    4. YOU DONT LOOK INTO C DISK RIGHT SAME WISE IF WE SEPARATE DATA BY PARTITION THEN IT INCREASE THE PERFORMANCE.
    5. HERE CREATE PARTITION BY RANGE METHOD.

CREATE TABLE ORDERS_PARTITION (
	ORDER_ID INT AUTO_INCREMENT,
	ORDER_DATE DATE NOT NULL,
	CUSTOMER_NAME VARCHAR(50),
	AMOUNT DECIMAL(10,2),
  PRIMARY KEY(ORDER_ID,ORDER_DATE)
)
PARTITION BY RANGE (YEAR (ORDER_DATE)) (
	PARTITION PARTITION_BEFORE_2020 VALUES LESS THAN (2020),
	PARTITION PARTITION_2020 VALUES LESS THAN (2021),
	PARTITION PARTITION_2021 VALUES LESS THAN (2022),
	PARTITION PARTITION_2022 VALUES LESS THAN (2023),
	PARTITION PARTITION_AFTER_2022 VALUES LESS THAN MAXVALUE
);

INSERT INTO ORDERS_PARTITION(ORDER_DATE,CUSTOMER_NAME,AMOUNT)
VALUES
('2019-05-10', 'ALICE', 100.00),
('2020-01-15', 'BOB', 200.50),
('2020-12-01', 'CHARLIE', 300.00),
('2021-07-20', 'DIANA', 150.75),
('2022-03-02', 'EDWARD', 500.00),
('2025-06-18', 'FUTUREMAN', 9999.99);

POINTS TO REMEMBER :

    1. IF SOMETIMES WE DONT KNOW ABOUT THIS TABLE HAS PARTITION OR NOT THAT TIME BELOW QUERY DISPLAY THE DATA ABOUT THE TABLE.
    2. OR YOU CAN USE SHOW CREATE TABLE 'TABLE_NAME' QUERY TO DISPLAY THE CREATE TABLE SCHEMA.

SELECT 
	PARTITION_NAME,PARTITION_METHOD,PARTITION_EXPRESSION,SUBPARTITION_METHOD,SUBPARTITION_EXPRESSION
FROM INFORMATION_SCHEMA.PARTITIONS
WHERE TABLE_SCHEMA = 'MYSQL_TUTORIAL' AND TABLE_NAME = 'ORDERS_PARTITION';

PARTITION_AFTER_2022	  RANGE	year(`order_date`)		NULL    NULL
PARTITION_2022	        RANGE	year(`order_date`)		NULL    NULL
PARTITION_2021	        RANGE	year(`order_date`)		NULL    NULL
PARTITION_2020	        RANGE	year(`order_date`)		NULL    NULL
PARTITION_BEFORE_2020	  RANGE	year(`order_date`)		NULL    NULL

SHOW CREATE TABLE ORDERS_PARTITION;

'CREATE TABLE `orders_partition` (
  `ORDER_ID` int NOT NULL AUTO_INCREMENT,
  `ORDER_DATE` date NOT NULL,
  `CUSTOMER_NAME` varchar(50) DEFAULT NULL,
  `AMOUNT` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ORDER_ID`,`ORDER_DATE`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/*!50100 PARTITION BY RANGE (year(`ORDER_DATE`))
(PARTITION PARTITION_BEFORE_2020 VALUES LESS THAN (2020) ENGINE = InnoDB,
 PARTITION PARTITION_2020 VALUES LESS THAN (2021) ENGINE = InnoDB,
 PARTITION PARTITION_2021 VALUES LESS THAN (2022) ENGINE = InnoDB,
 PARTITION PARTITION_2022 VALUES LESS THAN (2023) ENGINE = InnoDB,
 PARTITION PARTITION_AFTER_2022 VALUES LESS THAN MAXVALUE ENGINE = InnoDB) */'

NOTE : BELOW QUERY JUST DISPLAY THE DATA WITHOUT USING PARITIONS. LOOK AT THE JSON AND CHECK THE PARITIONS FIELDS. 
       IT SCAN ALL THE PARITIONS WHICH MEANS WHOLE TABLE FULL SCAN.
       IT TAKES TIMES.

SELECT * FROM ORDERS_PARTITION WHERE YEAR(ORDER_DATE) = 2021;

ORDER_ID    ORDER_DATE  CUSTOMER_NAME   AMOUNT
4	          2021-07-20	DIANA	          150.75

EXPLAIN FORMAT = JSON
SELECT * FROM ORDERS_PARTITION WHERE YEAR(ORDER_DATE) = 2021;

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "1.85"
    },
    "table": {
      "table_name": "ORDERS_PARTITION",
      "partitions": [
        "PARTITION_BEFORE_2020",
        "PARTITION_2020",
        "PARTITION_2021",
        "PARTITION_2022",
        "PARTITION_AFTER_2022"
      ],
      "access_type": "ALL",
      "rows_examined_per_scan": 6,
      "rows_produced_per_join": 6,
      "filtered": "100.00",
      "cost_info": {
        "read_cost": "1.25",
        "eval_cost": "0.60",
        "prefix_cost": "1.85",
        "data_read_per_join": "1K"
      },
      "used_columns": [
        "ORDER_ID",
        "ORDER_DATE",
        "CUSTOMER_NAME",
        "AMOUNT"
      ],
      "attached_condition": "(year(`mysql_tutorial`.`orders_partition`.`ORDER_DATE`) = 2021)"
    }
  }
}'

NOTE : BUT BELOW QUERY USED THE PARITIONS AS WELL. LOOK AT THE JSON IT JUST SCAN THE PARTICULAR PARITION ONLY.
       IT INCREASE THE PERFORMANCE BY THE TIME LOOK AT THE ABOVE TIME AND BELOW QUERY TIME.

SELECT * FROM ORDERS_PARTITION WHERE ORDER_DATE = '2021-07-20';

ORDER_ID    ORDER_DATE  CUSTOMER_NAME   AMOUNT
4	          2021-07-20	DIANA	          150.75

EXPLAIN FORMAT = JSON
SELECT * FROM ORDERS_PARTITION WHERE ORDER_DATE = '2021-07-20';

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.35"
    },
    "table": {
      "table_name": "ORDERS_PARTITION",
      "partitions": [
        "PARTITION_2021"
      ],
      "access_type": "ALL",
      "rows_examined_per_scan": 1,
      "rows_produced_per_join": 1,
      "filtered": "100.00",
      "cost_info": {
        "read_cost": "0.25",
        "eval_cost": "0.10",
        "prefix_cost": "0.35",
        "data_read_per_join": "216"
      },
      "used_columns": [
        "ORDER_ID",
        "ORDER_DATE",
        "CUSTOMER_NAME",
        "AMOUNT"
      ],
      "attached_condition": "(`mysql_tutorial`.`orders_partition`.`ORDER_DATE` = DATE''2021-07-20'')"
    }
  }
}'

# ----------------------------- 2. LIST PARTITION -------------------------

POINTS TO REMEMBER :

    1. HERE PARTITION BY LIST USED TO SEPARATE THE DATA BY DEPARTMENT.
    2. NOTE -> WHILE IN SELECT QUERY MUST USE THE PARTITION MENTIONED FIELD ONLY THEN ONLY PARTITION WILL WORK OTHER WISE IT WONT.
    3. FIRST SELECT QUERY USED NON PARTITIONED FIELD SO CHECK THE JSON IT SCAN ALL THE PARTITIONS SO IT TAKES MORE TIME AND LESS PERFORMANCE.
    4. NEXT SELECT QUERY USED PARTITIONED FIELD WHICH IS DEPARTMENT SO IT SCAN ONLY THE SELECT VALUES ONLY NOT FULL SCAN SO IMPROVES PERFORMANCE AND LOOK AT THE TIME.
    5. SEE THE DIFF B/W WITH OR WITHOUT PARTITION AT JSON FORMAT IT SHOWS THE DIFF.

CREATE TABLE EMPLOYEES_LIST_PARTITION(
	EMPLOYEE_ID INT AUTO_INCREMENT,
	FIRST_NAME VARCHAR(50),
	LAST_NAME VARCHAR(50),
	DEPARTMENT VARCHAR(50),
    PRIMARY KEY(EMPLOYEE_ID,DEPARTMENT)
)
PARTITION BY LIST COLUMNS(DEPARTMENT) (
	PARTITION SALES_TEAM VALUES IN ('SALES'),
	PARTITION HR_TEAM VALUES IN ('HR'),
	PARTITION ENG_TEAM VALUES IN ('ENGINEERING', 'DEVOPS'),
	PARTITION OTHERS_TEAM VALUES IN ('FINANCE', 'MARKETING', 'OPERATIONS')
);

INSERT INTO EMPLOYEES_LIST_PARTITION(FIRST_NAME, LAST_NAME, DEPARTMENT)
VALUES
('ALICE', 'SMITH', 'SALES'),
('BOB', 'JOHNSON', 'HR'),
('CHARLIE', 'LEE', 'ENGINEERING'),
('DIANA', 'LOPEZ', 'DEVOPS'),
('EVE','TURNER','Marketing');

EXPLAIN FORMAT = JSON
SELECT * FROM EMPLOYEES_LIST_PARTITION WHERE FIRST_NAME = 'BOB';

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "1.50"
    },
    "table": {
      "table_name": "EMPLOYEES_LIST_PARTITION",
      "partitions": [
        "SALES_TEAM",
        "HR_TEAM",
        "ENG_TEAM",
        "OTHERS_TEAM"
      ],
      "access_type": "ALL",
      "rows_examined_per_scan": 5,
      "rows_produced_per_join": 1,
      "filtered": "20.00",
      "cost_info": {
        "read_cost": "1.40",
        "eval_cost": "0.10",
        "prefix_cost": "1.50",
        "data_read_per_join": "616"
      },
      "used_columns": [
        "EMPLOYEE_ID",
        "FIRST_NAME",
        "LAST_NAME",
        "DEPARTMENT"
      ],
      "attached_condition": "(`mysql_tutorial`.`employees_list_partition`.`FIRST_NAME` = ''BOB'')"
    }
  }
}'

SELECT * FROM EMPLOYEES_LIST_PARTITION WHERE DEPARTMENT IN ('SALES','DEVOPS');

EXPLAIN FORMAT = JSON
SELECT * FROM EMPLOYEES_LIST_PARTITION WHERE DEPARTMENT IN ('SALES','DEVOPS');

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.80"
    },
    "table": {
      "table_name": "EMPLOYEES_LIST_PARTITION",
      "partitions": [
        "SALES_TEAM",
        "ENG_TEAM"
      ],
      "access_type": "ALL",
      "rows_examined_per_scan": 3,
      "rows_produced_per_join": 1,
      "filtered": "50.00",
      "cost_info": {
        "read_cost": "0.65",
        "eval_cost": "0.15",
        "prefix_cost": "0.80",
        "data_read_per_join": "924"
      },
      "used_columns": [
        "EMPLOYEE_ID",
        "FIRST_NAME",
        "LAST_NAME",
        "DEPARTMENT"
      ],
      "attached_condition": "(`mysql_tutorial`.`employees_list_partition`.`DEPARTMENT` in (''SALES'',''DEVOPS''))"
    }
  }
}'

# --------------------------------- HASH PARTITIONS ---------------------------------

POINTS TO REMEMBER :

    1. HERE HASH HOW ITS WORK ? FIRST OF WE GAVE NUMBER AT PARTITION HERE WE GAVE 2.
    2. AND PARTITION MENTIONED FOR SENSOR_ID SO WHILE INSERTING FIRST ROW CHECK THE SENSOR_ID AND MODULO THAT BY 2 AND TAKE THE REMAINDER AND CREATED PARTITION P0,P1 AUTOMATICALLY.
    3. FIRST ROW -> 101 % 2 -> IT GOES P1 PARTITION.
    4. SECOND ROW -> 102 % 2 -> IT GOES P0 PARTITION LIKE WISE ALL THE INSERTED ROWS.
    5. AND CHECK THE JSON FORMAT AT PARTITION FIELD TO UNDERSTAND THIS P0,P1 FOR EACH ROW.

CREATE TABLE SENSOR_DATA_HASH_PARTITION(
	SENSOR_ID INT NOT NULL,
    READING_TIME DATETIME NOT NULL,
    READING_VALUE DECIMAL(10,2),
    PRIMARY KEY(SENSOR_ID, READING_TIME)
)
PARTITION BY HASH(SENSOR_ID) PARTITIONS 2;

INSERT INTO SENSOR_DATA_HASH_PARTITION (SENSOR_ID, READING_TIME, READING_VALUE)
VALUES
(101, '2025-01-01 10:00:00', 23.50),
(102, '2025-01-01 10:05:00', 24.10),
(103, '2025-01-01 10:10:00', 22.75),
(104, '2025-01-01 10:15:00', 25.00),
(105, '2025-01-01 10:20:00', 20.00),
(106, '2025-01-01 10:25:00', 21.60);

EXPLAIN FORMAT = JSON
SELECT * FROM SENSOR_DATA_HASH_PARTITION WHERE SENSOR_ID = 101;

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.35"
    },
    "table": {
      "table_name": "SENSOR_DATA_HASH_PARTITION",
      "partitions": [
        "p1"
      ],
      "access_type": "ref",
      "possible_keys": [
        "PRIMARY"
      ],
      "key": "PRIMARY",
      "used_key_parts": [
        "SENSOR_ID"
      ],
      "key_length": "4",
      "ref": [
        "const"
      ],
      "rows_examined_per_scan": 1,
      "rows_produced_per_join": 1,
      "filtered": "100.00",
      "cost_info": {
        "read_cost": "0.25",
        "eval_cost": "0.10",
        "prefix_cost": "0.35",
        "data_read_per_join": "16"
      },
      "used_columns": [
        "SENSOR_ID",
        "READING_TIME",
        "READING_VALUE"
      ]
    }
  }
}'

EXPLAIN FORMAT = JSON
SELECT * FROM SENSOR_DATA_HASH_PARTITION WHERE SENSOR_ID = 102;

'{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.35"
    },
    "table": {
      "table_name": "SENSOR_DATA_HASH_PARTITION",
      "partitions": [
        "p0"
      ],
      "access_type": "ref",
      "possible_keys": [
        "PRIMARY"
      ],
      "key": "PRIMARY",
      "used_key_parts": [
        "SENSOR_ID"
      ],
      "key_length": "4",
      "ref": [
        "const"
      ],
      "rows_examined_per_scan": 1,
      "rows_produced_per_join": 1,
      "filtered": "100.00",
      "cost_info": {
        "read_cost": "0.25",
        "eval_cost": "0.10",
        "prefix_cost": "0.35",
        "data_read_per_join": "16"
      },
      "used_columns": [
        "SENSOR_ID",
        "READING_TIME",
        "READING_VALUE"
      ]
    }
  }
}'