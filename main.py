# 23919323 
# https://www.canva.com/design/DAFX7Kp6kFM/3bLJGKATsNgCQDvJfXB0qw/edit
import json

def load_data():
    with open("data.json", "r") as file:
        temp = json.load(file)
    return temp

def save_data(tempdata):
    with open("data.json", "w") as file:
        json.dump(tempdata, file, indent=4)

def load_songs_list():
    with open("list.json", "r") as file:
        temp = json.load(file)
    return temp

def load_artists():
    with open("artists.json", "r") as file:
        temp = json.load(file)
    return temp

def save_artists(tempdata):
    with open("artists.json", "w") as file:
        json.dump(tempdata, file, indent=4)

def load_albums():
    with open("albums.json", "r") as file:
        temp = json.load(file)
    return temp

def save_albums(tempdata):
    with open("albums.json", "w") as file:
        json.dump(tempdata, file, indent=4)



data = load_data()
artists = set(load_artists())
albums = load_albums()
last_stop = data["last_stop"]

songs_list = load_songs_list()
songs_list_len = len(songs_list)

for i, name in enumerate(songs_list):
    if (i < last_stop): 
        print(i + 1, name)
        continue
    print((i/(songs_list_len - 1)) * 100)
    x = input("Enter x to exit")
    if (x.lower() == "x"): break
    temp = {
        "title": name,
    }
    print(i + 1, name)
    original_name = input("Enter Song Name: ")
    artists_name = input("Enter Comma Sperated Artists Name: ")
    album = input("Enter Album Name: ")
    year = input("Enter Year: ")

    artists_name = artists_name.split(",")

    temp["original_name"] = original_name
    temp["artists_name"] = list(map(lambda name: name.strip(), artists_name))
    temp["album"] = album
    temp["year"] = year

    data['data'].append(temp)

    albums[album] = year
    for n in artists_name:
        artists.add(n)

    data["last_stop"] = i

    save_data(data)
    save_artists(list(artists))
    save_albums(albums)
    

data["last_stop"] = i

save_data(data)
save_artists(list(artists))
save_albums(albums)