def make_album(artist, album, songs=None):
    """Make an album"""
    album = {'artist': artist, 'album': album}
    if songs:
        album['songs'] = songs
    return album

while True:
    print("\nLet's create an Album:")
    print("(enter 'q' at any time to quit)")

    ar_name = input("Artist: ")
    if ar_name == 'q':
        break
    
    al_name = input("Album: ")
    if al_name == 'q':
        break

    n_songs = input("Songs: ")
    if n_songs == 'q':
        break

    the_album = make_album(ar_name, al_name, songs=n_songs)
    print(f"Your album: {the_album}.")