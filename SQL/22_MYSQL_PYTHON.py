# FIRST INSTALL MYSQL TO PYTHON -> pip install mysql-connector-python  

import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "HR"
)

try:
    if conn.is_connected:
        print("Database connected sucessfully\n")
        cursor = conn.cursor()
        query = "SELECT * FROM  EMPLOYEES"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

except mysql.connector.Error as e:
    print(f"Error : {e}")

finally:
    if conn.is_connected:
        cursor.close()
        conn.close()
        print("\nConnection disconnected successfully")

'''
Database connected sucessfully

(1, 'John', 'Doe', 'john.doe@example.com', datetime.date(2022, 5, 1), 'Software Engineer', Decimal('85000.00'))
(2, 'Jane', 'Smith', 'jane.smith@example.com', datetime.date(2023, 3, 15), 'Data Scientist', Decimal('92000.00'))
(3, 'Alice', 'Johnson', 'alice.johnson@example.com', datetime.date(2024, 5, 1), 'Engineer', Decimal('95000.00'))
(4, 'Mark', 'Taylor', 'mark.taylor@example.com', datetime.date(2022, 11, 15), 'Manager', Decimal('100000.00'))
(5, 'Gowtham', 'sb', 'mark.taylor@example.com', datetime.date(2022, 11, 15), 'Data Engineer', Decimal('100000.00'))
(6, 'Peter', 'sb', 'mark.taylor@example.com', datetime.date(2022, 11, 15), 'Data Engineer', Decimal('120000.00'))
(7, 'john', 'sb', 'mark.taylor@example.com', datetime.date(2022, 11, 15), 'Data Engineer', Decimal('120000.00'))

Connection disconnected successfully

'''