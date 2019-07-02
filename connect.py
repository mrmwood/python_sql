import mysql.connector

mydb = mysql.connector.connect(
  host="mwd.dubaicollegedev.me",
  user="mwd_pygame123",
  #pw: no1 location plus street num x 3
  passwd="",
  database="mwd_pygame"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
val = ("Bob", "Smith Street 1232")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
