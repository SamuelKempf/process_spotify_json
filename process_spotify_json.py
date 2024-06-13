"""
File: process_spotify_json.py
Author: Samuel Kempf
Date: 31-Dec-2023
Description: A Python script to convert Spotify extended streaming data from JSON to CSV for data analysis.
"""

import json

def main():
    f = open('spotify-extended.json', encoding='utf-8')

    data = json.load(f)

    headers = 'timestamp,artist,album,track,track_id' + '\n'

    file = open('spotify-extended.csv', 'ab')

    file.write(headers.encode('utf-8))'))

    for item in data:
        if item['skipped']:  # Don't process songs that were skipped.
            continue
        elif item['ms_played'] < 30000:  # Don't process songs that played for less than 30 seconds.
            continue
        elif item['incognito_mode']:  # Don't process songs that were listened to in incognito mode.
            continue

        track_URI = str(item['spotify_track_uri'])
        track_id = track_URI.replace('spotify:track:','')

        artist_name = escape_commas(str(item['master_metadata_album_artist_name']))
        album_name = escape_commas(str(item['master_metadata_album_album_name']))
        track_name = escape_commas(str(item['master_metadata_track_name']))

        line = str(item['ts']) + "," + artist_name + "," + album_name + "," + track_name + "," + track_id + '\n'
        file.write(line.encode('utf-8'))  # Write some text

    file.close()

# If the name of a band, album, or song includes commas, enclose it in double quotes so the CSV fields can be processed correctly.
def escape_commas(str):
    if ',' in str:
        str = "\"" + str + "\""

    return str

main()