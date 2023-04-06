# importing required libraries
import mysql.connector
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "guvidw28",
  database = "sakila"
)

mycursor = mydb.cursor()

#mycursor.execute('SHOW TABLES')

#for table in mycursor:
#    print(table[0])


mycursor.execute('select * from actor')
result = mycursor.fetchall()
for x in result:
    print(x[1], x[2])

