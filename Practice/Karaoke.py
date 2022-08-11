directions = "Enter (enter song title to add to queue... enter 'end' to stop adding songs... enter 'view queue' to view queue): "
song_name = input(directions)
songs = []

while (song_name != "end"):
    if (song_name == "view queue"):
        print("\nHere's your queue: ")
        while (len(songs) > 0):
            print(songs[0])
            songs.pop(0)
        print("end of queue\n")

    songs.append(song_name)

    if (song_name != "view queue"):
        song_name = input("\nNow playing: '{}',\n{}". format(song_name, directions))
    else:
        song_name = input(directions)
    