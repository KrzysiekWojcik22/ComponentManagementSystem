import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='KrzysiekmySql12',
    database="testsql"
)

mycursor = mydb.cursor()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)