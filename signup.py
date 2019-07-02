import connect
from hash import hash_password

#Get the user to enter their details
un = input("Username: ")
pw = input("Password: ")
yr = int(input("Year: "))

#Hash the password
hashed_pw = hash_password(pw)

sql = "INSERT INTO users (name, password, year) VALUES (%s, %s, %s)"
val = (un, hashed_pw, yr)
connect.mycursor.execute(sql, val)

connect.mydb.commit()

print(connect.mycursor.rowcount, "record inserted.")
