from operations import add_new_song,edit_song,search_song,delete_song,display_song
import json


def display_homepage(name):
        print("1:add a new song")
        print("2:edit existing song")
        print("3:search a song")
        print("4:delete a song")
        print("5:display all songs")
        print("6:Exit Application")
        choice=int(input("Enter your choice:\n"))
        if choice is 1:
            add_new_song(name)
            display_homepage(name)
        elif choice is 2:
            edit_song(name)
            display_homepage(name)
        elif choice is 3:
            search_song(name)
            display_homepage(name)
        elif choice is 4:
            delete_song(name)
            display_homepage(name)
        elif choice is 5:
            display_song(name)
            display_homepage(name)
        elif choice is 6:
                feedback(name)
                exit()
        else:
                feedback(name)
                exit()
        
def feedback(name):
        print("Please provide your feedback")
        rating=int(input("Provide rating between 0 to 10\n"))

        if rating<0 or rating>10 or rating=="":
                rating=int(input("Provide rating between 0 to 10\n"))

        readFile=open("feedback.json","r")

        decode=json.load(readFile)

        readFile.close()

        writeFile=open("feedback.json","w")

        data={
                "name":name,
                "rating":rating
              }

        decode.append(data)

        encode=json.dumps(decode)

        writeFile.write(encode)

        writeFile.close()
        
        print("Thanks for your feedback")



        












        
        
