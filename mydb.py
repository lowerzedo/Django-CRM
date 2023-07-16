import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678'

)

# CURSOR Object
cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute("CREATE DATABASE crmdb")

print("all done")