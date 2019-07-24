import json

def add_to_user(name,usr,pwd,email,mob):
    account_file=open('accounts.json','r')

    decode=json.load(account_file)

    account_file.close()
    
    data={
        "name":name,
        "username":usr,
        "password":pwd,
        "email":email,
        "mobile":mob
        }

    decode.append(data)
    
    encode=json.dumps(decode)

    new=open('accounts.json','w')
    
    new.write(encode)
    new.close()

                
