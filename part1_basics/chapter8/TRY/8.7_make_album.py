def make_album(artist, album, songs=None):
    """Make an album"""
    album = {'artist': artist, 'album': album}
    if songs:
        album['songs'] = songs
    return album

robbie = make_album("Robbie Williams", "Oostenrijk", songs=13)
print(robbie)

phil = make_album("Phil Collings", "Home")
print(phil)

queen = make_album("Queen", "Boheimian", songs=23)
print(queen)
