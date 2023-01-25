import mysql.connector

"""
DO NOT RUN MULTIPLE TIMES!! SAVING THIS JUST FOR MYSELF TO RE-CREATE THE DB ON THE SERVER IF NEEDED.
"""

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'Pass123'
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)