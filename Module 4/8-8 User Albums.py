def make_album(artist, title, song_number=None):
    if song_number == None:
        album = {"Artist": artist, "Title": title}
    else:
        album = {"Artist": artist, "Title": title, "Song Number": song_number}
    return album

answer = "n"
quit = "n"
while quit == "n":
    if answer == "n":
        user_artist = input("Please enter artist: ")
        user_title = input("Please enter album title: ")
        print(make_album(user_artist, user_title))
    elif answer == "y":
        break
    else:
        print("Please enter valid input")
    answer = input("Would you like to quit (y/n)?")
