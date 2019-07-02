import mysql.connector

mydb = mysql.connector.connect(
  host="mwd.dubaicollegedev.me",
  user="mwd_pygame123",
  #pw: no1 location plus street num x 3
  passwd="",
  database="mwd_pygame"
)

mycursor = mydb.cursor()
