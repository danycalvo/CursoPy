import mysql.connector


database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Ejx988mdc",
    database = "master_python"
)
print(database)
cursor = database.cursor()

cursor.execute("show databases")

for bd in cursor:
    print(bd)
