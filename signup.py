import connect
from hash import hash_password

exists = True

while exists == True:
    #Get the user to enter their details
    un = input("Username: ")
    pw = input("Password: ")
    yr = int(input("Year: "))

    exists = connect.check_username_exists(un)

#Hash the password
hashed_pw = hash_password(pw)

sql = "INSERT INTO users (username, password, year) VALUES (%s, %s, %s)"
val = (un, hashed_pw, yr)
connect.mycursor.execute(sql, val)

connect.mydb.commit()

print(connect.mycursor.rowcount, "record inserted.")
