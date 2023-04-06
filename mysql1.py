
# importing required libraries
import mysql.connector
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "guvidw28",
  #database = "datascience"
)

#print(mydb)

mycursor = mydb.cursor()

#Creating a database
#mycursor.execute("CREATE DATABASE tempdb")

#Checking the existing databases
mycursor.execute("SHOW DATABASES")

for x in mycursor:
      print(x[0])

#creating a table
#mycursor.execute("CREATE TABLE customer (name VARCHAR(255), address VARCHAR(255))")

#Display the existing tables



print("Done...")