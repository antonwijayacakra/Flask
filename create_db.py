import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
databases = mydb.cursor()
databases.execute("show databases")
for db in databases:
    print(db)