import connect
from hash import verify_password

un = input("Username: ")
pw = input("Password: ")

sql = "SELECT password FROM users WHERE username = %s"
adr = (un, )
connect.mycursor.execute(sql, adr)

myresult = connect.mycursor.fetchall()

#will get the hashed passord as a string from the database
#print(myresult[0][0])

#checks the hashed pw from the db against the one entered by the user
#print(verify_password(myresult[0][0], pw))

verified = verify_password(myresult[0][0], pw)

if verified == True:
    print("you're in")
else:
    print("please try again")
