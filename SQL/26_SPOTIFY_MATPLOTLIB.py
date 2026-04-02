# ----------------------------- SPOTIFY - MATPLOTLIB ---------------------------------------------

# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import pandas as pd
# import matplotlib.pyplot as plt
# import re

# # Set up Client Credentials
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#     client_id='c70480f479c44ccabe4696ea6367cce6',  # Replace with your Client ID
#     client_secret='771b783754a748ecba884e0999d7c262'  # Replace with your Client Secret
# ))

# # Full track URL (example: Shape of You by Ed Sheeran)
# track_url = "https://open.spotify.com/track/5BMXaTZOT3tI9PdyPVsTe6"

# # Extract track ID directly from URL using regex
# track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# # Fetch track details
# track = sp.track(track_id)
# print(track)

# # Extract metadata
# track_data = {
#     'Track Name': track['name'],
#     'Artist': track['artists'][0]['name'],
#     'Album': track['album']['name'],
#     'Popularity': track['popularity'],
#     'Duration (minutes)': track['duration_ms'] / 60000
# }

# # Display metadata
# print(f"\nTrack Name: {track_data['Track Name']}")
# print(f"Artist: {track_data['Artist']}")
# print(f"Album: {track_data['Album']}")
# print(f"Popularity: {track_data['Popularity']}")
# print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

# # Convert metadata to DataFrame
# df = pd.DataFrame([track_data])
# print("\nTrack Data as DataFrame:")
# print(df)

# # Save metadata to CSV
# df.to_csv('spotify_track_data.csv', index=False)

# # Visualize track data
# features = ['Popularity', 'Duration (minutes)']
# values = [track_data['Popularity'], track_data['Duration (minutes)']]

# plt.figure(figsize=(8, 5))
# plt.bar(features, values, color='skyblue', edgecolor='black')
# plt.title(f"Track Metadata for '{track_data['Track Name']}'")
# plt.ylabel('Value')
# plt.show()

# ----------------------------------- SPOTIFY - SINGLE TRACK ADDED INTO DB ---------------------------

# pip install mysql-connector-python
# pip install spotipy

# import pandas as pd
# import re
# import mysql.connector
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from mysql.connector.errors import Error

# conn = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '1234',
#     database = 'mysql_tutorial'
# )

# try:
#     if conn.is_connected():
#         print(f"Database connected successfully...!!!")
#         cursor = conn.cursor()

#         sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#             client_id='c70480f479c44ccabe4696ea6367cce6',
#             client_secret='771b783754a748ecba884e0999d7c262'
#         ))

#         track_url = "https://open.spotify.com/track/7LfIX3DCzl3AtGJWlCKOKK"

#         track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url)[1]

#         track = sp.track(track_id)

#         track_data = {
#             'Track Name': track['name'],
#             'Artist': track['artists'][0]['name'],
#             'Album': track['album']['name'],
#             'Popularity': track['popularity'],
#             'Duration (minutes)': track['duration_ms'] / 60000
#         }

#         # Insert data into MySQL
#         insert_query = """
#         INSERT INTO SPOTIFY_TRACKS (TRACK_NAME, ARTIST, ALBUM, POPULARITY, DURATION_MINUTES)
#         VALUES (%s, %s, %s, %s, %s)
#         """
#         cursor.execute(insert_query, (
#             track_data['Track Name'],
#             track_data['Artist'],
#             track_data['Album'],
#             track_data['Popularity'],
#             track_data['Duration (minutes)']
#         ))

#         conn.commit()

#         print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

# except Error as e:
#     print(f"Error : {e}")

# finally:
#         cursor.close()
#         conn.close()
#         print("Database closed successfully...!!!")

# ---------------------- SPOTIFY - IMPORT FROM TXT FILE ---------------------------

import pandas as pd
import re
import mysql.connector
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from mysql.connector.errors import Error

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'mysql_tutorial'
)

try:
    if conn.is_connected():
        print(f"Database connected successfully...!!!")
        cursor = conn.cursor()

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id='c70480f479c44ccabe4696ea6367cce6',
            client_secret='771b783754a748ecba884e0999d7c262'
        ))

        # Read track URLs from file
        file_path = "track_urls.txt"
        with open(file_path, 'r') as file:
            track_urls = file.readlines()

        for track_url in track_urls:
            track_url = track_url.strip()  # Remove any leading/trailing whitespace
            track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url)[1]

            track = sp.track(track_id)

            track_data = {
                'Track Name': track['name'],
                'Artist': track['artists'][0]['name'],
                'Album': track['album']['name'],
                'Popularity': track['popularity'],
                'Duration (minutes)': track['duration_ms'] / 60000
            }

            # Insert data into MySQL
            insert_query = """
            INSERT INTO SPOTIFY_TRACKS (TRACK_NAME, ARTIST, ALBUM, POPULARITY, DURATION_MINUTES)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                track_data['Track Name'],
                track_data['Artist'],
                track_data['Album'],
                track_data['Popularity'],
                track_data['Duration (minutes)']
            ))

            conn.commit()

            print(f"Track '{track_data['Track Name']}' by {track_data['Artist']} inserted into the database.")

except Error as e:
    print(f"Error : {e}")

finally:
        cursor.close()
        conn.close()
        print("Database closed successfully...!!!")