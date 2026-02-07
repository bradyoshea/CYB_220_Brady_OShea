def make_album(artist, title, song_number=None):
    """This function describes an album based on the input parameters"""
    if song_number == None:
        album = {"Artist": artist, "Title": title}
    else:
        album = {"Artist": artist, "Title": title, "Song Number": song_number}
    return album

print(make_album("The Kid LAROI", "THE FIRST TIME", "20"))
print(make_album("Djo", "DECIDE"))
print(make_album("Tyler, The Creator", "Flower Boy"))