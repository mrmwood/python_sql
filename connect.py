import mysql.connector

mydb = mysql.connector.connect(
  host="mwd.dubaicollegedev.me",
  user="mwd_pygame123",
  #pw: no1 location plus street num x 3
  passwd="",
  database="mwd_pygame"
)

mycursor = mydb.cursor()


#check if username already exists
def check_username_exists(un):
    #print("username is: ", un)
    sql = "SELECT COUNT(*) from users where username = %s"
    adr = (un, )
    mycursor.execute(sql, adr)

    result = mycursor.fetchone()

    #print("result is: ", result)
    if result[0] != 0:
        print("username already exists please try another one")
        return True
    else:
        print("Account Created")
        return False
