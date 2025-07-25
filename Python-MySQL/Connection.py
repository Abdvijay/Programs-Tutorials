import mysql.connector

conn = mysql.connector.connect(host="localhost", user = "root", passwd = "1234", database = "python_mysql")

cursor = conn.cursor()

cursor.execute('select * from student')

result = cursor.fetchall()

for i in result:
    print(i)