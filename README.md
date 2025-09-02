# 🎵 Music Recommendation System – Data Interface-with python
simple database for buying music
🎵 Music Recommendation System – Data Interface

This project is part of a Music Recommendation System being developed by the fictional company Queratoons.

The AI core of the system is already implemented, but to make use of raw data (users and albums), we need a data interface that connects them to the AI. This project implements that interface and provides query functions to process and prepare data for the recommendation engine.

⚙️ Project Structure

The system works with two main types of data:

User → username, age, city, and a list of purchased albums.

Album → album name, artist, genre, and number of tracks.

Data is stored using the helper functions add_user and add_album inside two structures: all_users and all_albums.

📌 Implemented Functions
1. Adding Data

add_user(username, age, city, albums, all_users)
→ Adds a new user to the user list.

add_album(name, artist, genre, tracks, all_albums)
→ Adds a new album to the album list.

2. Query Functions

These functions calculate the number of purchased tracks under different conditions:

query_user_artist(username, artist, all_users, all_albums)
→ Number of tracks purchased by a specific user from a given artist.

query_user_genre(username, genre, all_users, all_albums)
→ Number of tracks purchased by a specific user in a given genre.

query_age_artist(age, artist, all_users, all_albums)
→ Total tracks purchased by all users of a specific age from a given artist.

query_age_genre(age, genre, all_users, all_albums)
→ Total tracks purchased by all users of a specific age in a given genre.

query_city_artist(city, artist, all_users, all_albums)
→ Total tracks purchased by users living in a given city from a specific artist.

query_city_genre(city, genre, all_users, all_albums)
→ Total tracks purchased by users living in a given city in a given genre.
code:
all_users = []
all_albums = []

add_user("SAliB", 19, "Tehran", ["tekunbede", "barf", "gavazn"], all_users)
add_user("Saeid", 22, "Esfehan", ["eclipse", "barf", "gavazn"], all_users)

add_album("eclipse", "malmsteen", "classic", 10, all_albums)
add_album("barf", "beeptunes", "pop", 22, all_albums)
add_album("tekunbede", "beeptunes", "pop", 14, all_albums)
add_album("gavazn", "sorena", "persian", 18, all_albums)

add_user("Ali", 12, "Bushehr", ["bidad", "blaze"], all_users)
add_album("bidad", "shajarian", "classic", 10, all_albums)
add_album("blaze", "ghorbani", "pop", 9, all_albums)

print(query_user_artist("Ali", "ghorbani", all_users, all_albums))  # 9
print(query_user_genre("Ali", "classic", all_users, all_albums))   # 10
print(query_age_artist(12, "shajarian", all_users, all_albums))   # 10
print(query_age_genre(12, "pop", all_users, all_albums))          # 9
print(query_city_artist("Bushehr", "ghorbani", all_users, all_albums)) # 9
print(query_city_genre("Bushehr", "pop", all_users, all_albums))       # 9

How to Run

Clone the repository:

git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME


Run the test script:

python main.py

🎯 Purpose

This project provides a data interface layer for a music recommendation system. It transforms raw user and album data into structured information that can be consumed by the AI engine.

Future improvements may include:

Integration with a real database

REST API endpoints for external access

Expansion to support additional user and album metadata
