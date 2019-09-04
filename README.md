# python_sql

## will need to run pipenv to get the environment going
In command line go to the directory where the Pipfile is
then type in pipenv shell to activate the environment

## connect.py
contains the necessary details to access the remote database
make sure that you do not make these viewable when pushing to GitHub
At School you will need unblock the IP address on the dubaicollege devserver
to do this login into the dev server cpanel and on the dashboard click on Remote MYSQL
find your IP address by typing in Google MyIP and then enter this in the Host field on cpanel

# signup.py
Allows you to create an account with username, password and year
will inform you if the account has been added

# login.py
Try typing in an existing users UN and PW and all should be ok
Have found a problem when testing with non registered user if pw entered is short
A list index out of range error occurs?? 4-9-19

# hash.py
hashes and de-hashes the password when sending and receiving 
