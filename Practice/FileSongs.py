with open("songs.txt", "w") as w_file:
    # songs = input()
    # while (songs != "end"):
    #     w_file.write("{} \n".format(songs))
    #     songs = input()

    for x in range(1, 11):
        w_file.write("Song #{} \n".format(x))