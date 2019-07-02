import connect
from hash import hash_password

un = input("Username: ")
pw = input("Password: ")
#Hash the password
hashed_pw = hash_password(pw)
print(hashed_pw)

sql = "SELECT * FROM users WHERE name = %s AND password = %s"
adr = (un, hashed_pw)
connect.mycursor.execute(sql, adr)

myresult = connect.mycursor.fetchall()

for x in myresult:
  print(x)


# NOTE: Hashing algorithm is creating a different hash value each time the same value is hashed which it shouldn't.
# Need to look at alternative hashing algorithms for Python or look over the current one I am using
