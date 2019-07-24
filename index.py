from account import signup,login



class SongLibrary:
    def __init__(self,choice):
        self.choice=choice
        
        
    def proceed(self):
        if self.choice is 1:
            signup()
        elif self.choice is 2:
            login()
        elif self.choice is 3:
            exit()
        else: 
            exit()


print("Version: 1.2")
print("Credits: Adarsh n bidari")
print("Enter your choice")
choice=int(input("1:Signup 2:Login 3:exit\n"))


slib=SongLibrary(choice)
slib.proceed()

