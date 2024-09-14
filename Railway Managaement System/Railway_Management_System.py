# RAILWAY MANAGEMENT SYSTEM
# Importing Modules
import mysql.connector as sql
from random import randint
# Establishment of connection to MySQL Server
con = sql.connect(host="Your Host Name",
user="Your User",
password="Password",
database="Railway")   #Database Name(In my case it is Railway)
cur=con.cursor()
con.autocommit = True

#### Creation of Database and subsequent Tables
##cur.execute("CREATE DATABASE Railway;")
##cur.execute("USE Railway;")
##s = "CREATE TABLE accounts(ID int primary key,Password varchar(16),Name varchar(100),Sex char(1),Age int,DOB date,Ph_no varchar(10));"
##cur.execute(s)
##s = "CREATE TABLE tickets(ID int,PNR int,Train varchar(50),DOJ date,Travel_from varchar(100),Travel_to varchar(100),foreign key(ID) references accounts(ID));"
##cur.execute(s)

# Login Menu
def login_menu():
print("**********WELCOME TO THE Railway PORTAL**********")
print("1. Create New Account \n"
"2. Log In \n"
"3. Exit")
opt = int(input("Enter your choice: "))
if opt == 1:
create_acc()
elif opt == 2:
login()
elif opt == 3:
e = input("Exit the portal? (Y/N) ")
if e in "Nn":
login_menu()
if e in "Yy":
pass
else:
print("Enter a valid option !!")
else:
print("Enter a valid option !!")

# Account Creation

def create_acc():
print("Enter the details to create your account:")
i = randint(1000, 10000)
print("Your generated ID is:",i)
p = input("Enter your password: ")
n = input("Enter your name: ")
sex = input("Enter your gender (M/F/O): ")
sex=sex.upper()
age = int(input("Enter your age: "))
dob = input("Enter your date of birth (YYYY-MM-DD): ")
ph = input("Enter your contact number: ")
data=(i,p,n,sex,age,dob,ph)
sq ="insert into accounts
values('%d','%s','%s','%s','%d','%s','%s')"%(i,p,n,sex,age,dob,ph)
cur.execute(sq)
print("Now you may log in with your newly created account!")
login()

# Log in to Account
def login():
global a
try:
a = int(input("Enter your ID: "))
b = input("Enter your password: ")
s2 = "SELECT name FROM accounts WHERE ID = '%d' AND Password='%s';"%(a,b)
cur.execute(s2)
j = cur.fetchone()
print("Welcome back ",j[0],"!!")
main_menu()
except:
print("Your account was not found!")
print("You can: \n"
"1. Try logging in again \n"
"2. Create a new account")
ch = input("Enter your choice: ")
if ch == "1":
login()
elif ch == "2":
create_acc()
else:
print("Invalid choice!")
x1 = input("Exit the portal? (Y/N) ")
if x1 in "Nn":
login_menu()

# Main Menu
def main_menu():
print("**********What would you like to do today?********** \n"
"1. Purchase a Ticket \n"

"2. Check Ticket Status \n"
"3. Request a refund \n"
"4. Account Settings \n"
"5. Logout \n"
"6. Exit" )
ch1 = int(input("Enter your choice: "))
if ch1 == 1:
buy_ticket()
elif ch1 == 2:
show_ticket()
elif ch1 == 3:
cancel_ticket()
elif ch1 == 4:
account()
elif ch1 == 5:
login_menu()
else:
exit_prompt()

# Exit Prompt
def exit_prompt():
x2 = input("Would you like to exit? (Y/N) ")
if x2.upper() == "N":
main_menu()
elif x2.upper() == "Y":
pass
else:
print("Enter a Valid Option")

# Back to Main Menu
def back_to_main_menu():
x3 = input("Return to the Main Menu? (Y/N) ")
if x3.upper() == "Y":
print("Returning to Main Menu...")
main_menu()
elif x3.upper() == "N":
pass
else:
print("Enter a Valid Option")

# Ticket Creation
def buy_ticket():
print("Enter details for your journey: ")
i = a
pnr = randint(100000, 1000000)
print("Your PNR is :",pnr)
train = input("Enter the name of the train: ")

doj = input("Enter the date of your journey (YYYY-MM-DD): ")
fr = input("Enter the Departing Station: ")
to = input("Enter the Destination Station: ")
data2=(i,pnr,train,doj,fr,to)
s4 = "insert into tickets
values('%d','%d','%s','%s','%s','%s');"%(i,pnr,train,doj,fr,to)
cur.execute(s4)
back_to_main_menu()
# Ticket Checking
def show_ticket():
try:
pnr = int(input("Enter your PNR: "))
s5 = "SELECT * FROM tickets WHERE PNR = '%d'"%(pnr)
cur.execute(s5)
j = cur.fetchone()
if j[0] == a:
print("Train: ",j[2]," \n"
"Date of Journey: ",j[3],"\n"
"From: ",j[4],"\n"
"To: ",j[5])
back_to_main_menu()
else:
print("Unauthorized! \n"
"Your ID does not match the PNR of ticket.")
back_to_main_menu()
except:
ticket_not_found()

# Ask for a refund
def cancel_ticket():
try:
pnr = int(input("Enter the PNR number of the ticket: "))
s2 = "SELECT ID, PNR, Train FROM tickets WHERE PNR = '%d'"%(pnr)
cur.execute(s2)
j = cur.fetchone()
if j[0] == a:
print("PNR: ",j[1],"\n"
"Train: ",j[2])
x4 = input("Do you really want to cancel this ticket? (Y/N) ")
x4=x4.upper()
if x4 == "Y":
s3 = "DELETE FROM tickets WHERE PNR = '%d'"%(pnr)
cur.execute(s3)
print("You will be refunded shortly!")
back_to_main_menu()
elif x4 == "N":
back_to_main_menu()
else:
print("Enter a valid option !!")

back_to_main_menu()
else:
print("Unauthorized! \n"
"Your ID does not match "
"the PNR of ticket.")
back_to_main_menu()
except:
ticket_not_found()

# If ticket is not found
def ticket_not_found():
print("Ticket not found!")
print("You can: \n"
"1. Try entering your PNR number again \n"
"2. Purchase a ticket \n"
"3. Return to Main Menu \n"
"4. Exit")
ch = int(input("Enter your choice: "))
if ch == 1:
cancel_ticket()
elif ch == 2:
buy_ticket()
elif ch == 3:
print("Returning to Main Menu...")
main_menu()
elif ch == 4:
exit_prompt()
else:
print("Enter a valid option")
back_to_main_menu()

# Account settings
def account():
print("Do you want to: \n",
"1. Show Account details \n",
"2. Delete Account")
ch = int(input("Enter your choice: "))
if ch == 1:
s4 = "SELECT * FROM accounts WHERE id = '%d'"%(a)
cur.execute(s4)
j = cur.fetchone()
print("ID: ",j[0],"\n",
"Name: ",j[2],"\n",
"Gender: ",j[3],"\n",
"Age: ",j[4],"\n",
"DOB: ",j[5],"\n",
"Phone Number: ",j[6])
back_to_main_menu()

elif ch == 2:
x6 = input("Do you want to request for refund(s) for your ticket(s) too?
(Y/N) ")
if x6.upper() == "Y":
s5 = "DELETE FROM tickets WHERE id = '%d'"%(a)
cur.execute(s5)
print("You will be refunded shortly!")
elif x6.upper() == "N":
pass
else:
pass
s6 = "DELETE FROM accounts WHERE ID = '%d'"%(a)
cur.execute(s6)
print("Account Successfully Deleted!")
login_menu()
else:
back_to_main_menu()

# Calling the first function, hence starting the program
login_menu()