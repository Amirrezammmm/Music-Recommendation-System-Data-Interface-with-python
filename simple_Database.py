all_users = {}
all_albums = {}


def add_user(username, age, city, album: list, all_user, add_album):
    all_user[username] = {'age': age, 'city': city, 'album': album}


def add_album(album_name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[album_name] = {
        'artist_name': artist_name, 'genre': genre, 'tracks': tracks}


def query_user_artist(username, artist_name, all_users, all_albums):
    album = []
    Track = 0
    for names in all_users:
        if username == names:
            name = all_users[names]
            album = name.get('album')
    for items in album:
        for itemes in all_albums:
            if items == itemes:
                albumitems = all_albums[itemes]
                if albumitems.get('artist_name') == artist_name:
                    Track += albumitems.get('tracks')
    return Track


def query_user_genre(username, genre, all_users, all_albums):
    album = []
    Track = 0
    for names in all_users:
        if username == names:
            name = all_users[names]
            album = name.get('album')
    for items in album:
        for itemes in all_albums:
            if items == itemes:
                albumitems = all_albums[itemes]
                if albumitems.get('genre') == genre:
                    Track += albumitems.get('tracks')
    return Track


def query_age_artist(age, artist_name, all_users, all_albums):
    Tracks = 0
    userAlbums = []
    for users in all_users:
        user = all_users[users]
        if user.get('age') == age:
            userAlbums += user.get('album')
    for albums in all_albums:
        album = all_albums[albums]
        for items in userAlbums:
            if albums == items:
                if album.get('artist_name') == artist_name:
                    Tracks += album.get('tracks')
    return Tracks


def query_age_genre(age, genre, all_users, all_albums):
    Tracks = 0
    userAlbums = []
    for users in all_users:
        user = all_users[users]
        if user.get('age') == age:
            userAlbums += user.get('album')
    for albums in all_albums:
        album = all_albums[albums]
        for items in userAlbums:
            if albums == items:
                if album.get('genre') == genre:
                    Tracks += album.get('tracks')
    return Tracks


def query_city_artist(city, artist_name, all_users, all_albums):
    Tracks = 0
    userAlbums = []
    for users in all_users:
        user = all_users[users]
        if user.get('city') == city:
            userAlbums += user.get('album')
    for albums in all_albums:
        album = all_albums[albums]
        for items in userAlbums:
            if albums == items:
                if album.get('artist_name') == artist_name:
                    Tracks += album.get('tracks')
    return Tracks


def query_city_genre(city, genre, all_users, all_albums):
    Tracks = 0
    userAlbums = []
    for users in all_users:
        user = all_users[users]
        if user.get('city') == city:
            userAlbums += user.get('album')
    for albums in all_albums:
        album = all_albums[albums]
        for items in userAlbums:
            if albums == items:
                if album.get('genre') == genre:
                    Tracks += album.get('tracks')
    return Tracks


add_album("bidad", "shajarian", "classic", 10, all_users, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_users, all_albums)
add_album("eclipse", "malmsteen", "classic", 10, all_users, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_users, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_users, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_users, all_albums)
add_user('Amir', 22, 'Karaj', ['bidad', 'blaze'], all_users, all_albums)
add_user('Mahdi', 16, 'Karaj', ['bidad', 'blaze'], all_users, all_albums)
add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users, all_albums)
add_user("SAliB", 19, "Tehran", ["tekunbede",
         "barf", "gavazn",], all_users, all_albums)
add_user("Saeid", 22, "Esfehan", ["eclipse",
         "barf", "gavazn"], all_users, all_albums)
print(query_user_artist("Mahdi", "ghorbani", all_users, all_albums))
print(query_user_genre("SAliB", "pop", all_users, all_albums))
print(query_age_artist(22, "malmsteen", all_users, all_albums))
print(query_age_genre(12, "pop", all_users, all_albums))
print(query_age_genre(19, "pop", all_users, all_albums))
print(query_city_artist("Bushehr", "ghorbani", all_users, all_albums))
print(query_city_artist("Tehran", "sorena", all_users, all_albums))
print(query_city_genre("Bushehr", "pop", all_users, all_albums))
print(query_city_genre("Tehran", "pop", all_users, all_albums))
print(query_user_artist("SAliB", "beeptunes", all_users, all_albums))
