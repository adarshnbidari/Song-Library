import re



def validatePassword(pwd):
    pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@_]).{8,}"


    check=re.search(pattern,pwd)

    if check:
        return True
    else:
        return False


