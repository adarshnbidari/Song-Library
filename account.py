from login import verify_login 
from homepage import display_homepage
from insert import add_to_user
from password_validation import validatePassword
from email_validation import validateEmail
import json

def not_empty(arg):
    while arg is "":
        arg=input("Above field cannot be empty\n")

def signup():

    invalidPasswordAttempts=0
    invalidMobileNumberAttempts=0
    
    name=str(input("Enter your name\n"))
    not_empty(name)
    usr=str(input("Enter your username\n"))
    not_empty(usr)

    file=open("accounts.json","r")

    decode=json.load(file)

    exist=0
    
    if len(decode)>0:
        for i in decode:
            if i["username"]==usr:
                exist=1

    if exist is 1:
        print("User already exists!..., Please try other username")
        signup()
    
    print("Enter your password")
    pwd=input("Your password must contain atleast a uppercase,lowercase,number,@ or _ and minimum of lenghth 8\n")
    not_empty(pwd)
    while validatePassword(pwd) is False:
        if invalidPasswordAttempts<3:
            pwd=input("Enter a valid password\n")
            invalidPasswordAttempts+=1
        else:
            print("Too many attempts try again later")
            signup()
        
    cpwd=input("Please re-enter your password\n")
    not_empty(cpwd)
    while cpwd!=pwd:
        cpwd=input("Please re-enter your password\n")
    email=input("Enter your email\n")
    not_empty(email)
    while validateEmail(email) is False:
        email=input("Please enter a valid email\n")
    mob=int(input("Enter your mobile number\n"))
    not_empty(mob)
    while len(str(mob))!=10:
        if invalidMobileNumberAttempts<3:
            mob=int(input("Enter a valid mobile number\n"))
            invalidMobileNumberAttempts+=1
        else:
            print("too many attempts please try again later!...")
            signup()


    
    
    print("{} You have registered successfully!..".format(name))
    add_to_user(name,usr,pwd,email,mob)
    display_homepage(name)
 
        

def login():
    usr=str(input("Enter your username"))
    pwd=input("Enter your password")
    verify_login(usr,pwd)
    
