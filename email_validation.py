import re

def validateEmail(email):

    pattern="^[a-zA-Z]+[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,}"


    check=re.search(pattern,email)

    if not check:
        return False

