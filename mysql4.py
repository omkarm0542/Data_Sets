# importing required libraries
import mysql.connector
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "guvidw28",
  database = "dw40"
)

#print(mydb)

mycursor = mydb.cursor()

ipname = input("Enter name : ")
query = "insert into members(name) values( '" + str(ipname) +"')"
#print(query)
#Checking the existing databases
mycursor.execute(query)

mycursor.execute("commit;")
print("Done....")