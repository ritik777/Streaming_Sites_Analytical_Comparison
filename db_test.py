import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#Created Database
mycursor.execute("CREATE DATABASE streaming_analytics_db")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
