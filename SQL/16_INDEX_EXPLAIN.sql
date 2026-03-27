# ---------------------------------- INDEX AND EXPLAIN ------------------------------

# ----------------------------------- WITH USING ------------------------------------

CREATE TABLE CUSTOMERS_INDEX(
	CUSTOMER_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(20) NOT NULL,
    LAST_NAME VARCHAR(20) NOT NULL,
    EMAIL VARCHAR(100) NOT NULL,
    CITY VARCHAR(100) NOT NULL
);

POINTS TO REMEMBER :

    1.CREATE INDEX WHICH IS MOSTLY USED FIELD IN WHERE CLAUSE.
    2.IT WORKS ONLY ON MILLIONS OF RECORDS. MAINLY USED FOR PERFORMANCE.

CREATE INDEX IDX_EMAIL ON CUSTOMERS_INDEX(EMAIL);

INSERT INTO CUSTOMERS_INDEX(FIRST_NAME, LAST_NAME, EMAIL, CITY)
VALUES
(
'John', 'Doe', 'john@example.com', 'New York'),
('Jane', 'Smith', 'jane.smith@example.com', 'Los Angeles'),
('Michael', 'Brown', 'michael.brown@example.com', 'Chicago'),
('Emily', 'Johnson', 'emily.johnson@example.com', 'Houston'),
('Robert', 'Green', 'robert.green@example.com', 'Phoenix');


SELECT * FROM CUSTOMERS_INDEX WHERE EMAIL = 'john@example.com';

EXPLAIN
SELECT * FROM CUSTOMERS_INDEX WHERE EMAIL = 'john@example.com';

ID      SELECT_TYPE     TABLE               PARTITIONS      TYPE   POSSIBLE_KEYS      KEY         KEY_LEN     REF     ROWS      FILDERED      EXTRA
1	    SIMPLE	        CUSTOMERS_INDEX		                ref	   IDX_EMAIL	      IDX_EMAIL   402	      const	  1	        100.00	

EXPLAIN ANALYZE
SELECT * FROM CUSTOMERS_INDEX WHERE EMAIL = 'john@example.com';

'-> Index lookup on CUSTOMERS_INDEX using IDX_EMAIL (EMAIL=''john@example.com'')  
                    (cost=0.35 rows=1) (actual time=0.0387..0.0421 rows=1 loops=1)
'

EXPLAIN FORMAT = JSON
SELECT * FROM CUSTOMERS_INDEX WHERE EMAIL = 'john@example.com';

{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.35"
    },
    "table": {
      "table_name": "CUSTOMERS_INDEX",
      "access_type": "ref",
      "possible_keys": [
        "IDX_EMAIL"
      ],
      "key": "IDX_EMAI",
      "used_key_parts": [
        "EMAIL"
      ],
      "key_length": "402",
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
        "data_read_per_join": "976"
      },
      "used_columns": [
        "CUSTOMER_ID",
        "FIRST_NAME",
        "LAST_NAME",
        "EMAIL",
        "CITY"
      ]
    }
  }
}

# ------------------------------- WITHOUT USING INDEX ----------------------------

CREATE TABLE CUSTOMERS_INDEX_1(
	CUSTOMER_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(20) NOT NULL,
    LAST_NAME VARCHAR(20) NOT NULL,
    EMAIL VARCHAR(100) NOT NULL,
    CITY VARCHAR(100) NOT NULL
);

INSERT INTO CUSTOMERS_INDEX_1(FIRST_NAME, LAST_NAME, EMAIL, CITY)
VALUES
(
'John', 'Doe', 'john@example.com', 'New York'),
('Jane', 'Smith', 'jane.smith@example.com', 'Los Angeles'),
('Michael', 'Brown', 'michael.brown@example.com', 'Chicago'),
('Emily', 'Johnson', 'emily.johnson@example.com', 'Houston'),
('Robert', 'Green', 'robert.green@example.com', 'Phoenix');

EXPLAIN
SELECT * FROM CUSTOMERS_INDEX_1 WHERE EMAIL = 'john@example.com';

ID      SELECT_TYPE     TABLE                PARTITIONS      TYPE   POSSIBLE_KEYS      KEY         KEY_LEN     REF     ROWS      FILDERED      EXTRA
'1',    'SIMPLE',       'CUSTOMERS_INDEX_1', NULL,           'ALL', NULL,              NULL,       NULL,       NULL,   '5',     '20.00',       'Using where'

EXPLAIN ANALYZE
SELECT * FROM CUSTOMERS_INDEX_1 WHERE EMAIL = 'john@example.com';

'-> Filter: (customers_index_1.EMAIL = ''john@example.com'')  (cost=0.75 rows=1) (actual time=0.0654..0.0726 rows=1 loops=1)
    -> Table scan on CUSTOMERS_INDEX_1  (cost=0.75 rows=5) (actual time=0.0624..0.0687 rows=5 loops=1)
'

EXPLAIN FORMAT = JSON
SELECT * FROM CUSTOMERS_INDEX_1 WHERE EMAIL = 'john@example.com';

{
  "query_block": {
    "select_id": 1,
    "cost_info": {
      "query_cost": "0.75"
    },
    "table": {
      "table_name": "CUSTOMERS_INDEX_1",
      "access_type": "ALL",
      "rows_examined_per_scan": 5,
      "rows_produced_per_join": 1,
      "filtered": "20.00",
      "cost_info": {
        "read_cost": "0.65",
        "eval_cost": "0.10",
        "prefix_cost": "0.75",
        "data_read_per_join": "976"
      },
      "used_columns": [
        "CUSTOMER_ID",
        "FIRST_NAME",
        "LAST_NAME",
        "EMAIL",
        "CITY"
      ],
      "attached_condition": "(`mysql_tutorial`.`customers_index_1`.`EMAIL` = ''john@example.com'')"
    }
  }
}