import json

def add_new_song(name):
    song=input("Enter song to add\n")
    decode=""
    with open('songs.json','r') as json_file:
        decode=json.load(json_file)

    write_file=open('songs.json','w')

    data={
        "name":name,
        "song":song
        }
    decode.append(data)

    encode=json.dumps(decode)
    
    write_file.write(encode)
    write_file.close()
    print("{} has been added to your account successfully".format(song))

#add_new_song("suhas")


def search_song(name):
    song=input("Enter song to search\n")
    file=open('songs.json','r')
    decode=json.load(file)

    print("Loading...")
    
    for i in decode:
        if i["song"]==song:
            print("{}=>{}".format(i["name"],i["song"]))
            
#search_song("suhas")


def edit_song(name):
    prevSong=input("Enter existing song to it\n")
    song=input("Enter the new song\n")
    file=open('songs.json','r')
    
    decode=json.load(file)

    for i in decode:
        if i["name"]==name and i["song"]==prevSong:
            i["song"]=song

    file.close()

    encode=json.dumps(decode)

    update_songs=open('songs.json','w')

    update_songs.write(encode)
    update_songs.close()

    print("Your song has been updated successfully")

#edit_song("suhas")


def delete_song(name):
    song=input("Enter song to delete\n")
    file=open('songs.json','r')

    decode=json.load(file)

    new_data=[]

    for i in decode:
        if i["song"]==song:
            continue
        else:
            new_data.append(i)

    encode=json.dumps(new_data)

    file.close()

    update_songs=open('songs.json','w')

    update_songs.write(encode)
    update_songs.close()
    print("Song {} has been successfully deleted".format(song))

#delete_song("suhas")

def display_song(name):
    file=open('songs.json','r')

    decode=json.load(file)

    print("Dear {} you have below listed songs in your account".format(name))

    num=0
    
    for i in decode:

        num+=1
        
        print("{} : {}".format(num,i["song"]))


#display_song()


    

    

      
        
        


     

     

    
    




        
        
        
    
