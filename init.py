files=["accounts.json","songs.json","feedback.json"]

for file in files:
    f=open(file,"w")
    f.write("[]")
    f.close()

    
