import json
from homepage import display_homepage

def verify_login(usr,pwd):


    invalidLoginAttempts=0
    
    file=open('accounts.json','r')

    decode=json.load(file)


    exists=0
    
    for i in decode:
        if i["username"]==usr and i["password"]==pwd:
            display_homepage(i["name"])
            exists=1


    if exists is 0:
        print("Invalid username or password")
        username=input("Enter your username")
        password=input("Enter your password")

        verify_login(username,password)

