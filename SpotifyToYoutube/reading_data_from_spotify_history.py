import json

TRACK_NAME = 'trackName'
ARTIST_NAME = 'artistName'


def populate_raw_list(streaming_history: list) -> list:
    """
    :param streaming_history: the list parsed from the json.load() module
    :return: a raw `list` of (artist-track) sets
    """
    raw_list = []
    # Access the track name and the artist name and populating track_and_artist_raw_list
    for streaming_history_row in streaming_history_load:
        track_name = streaming_history_row[TRACK_NAME]
        artist_name = streaming_history_row[ARTIST_NAME]
        raw_list.append((artist_name, track_name))
    return raw_list


def remove_duplicate_items(track_artist_raw_list: list) -> list:
    """
    This function removes all duplicates (track-artist) sets from the track_and_artist_raw_list
    and return a list of unique (artist-track) sets
    :param track_artist_raw_list: the list to remove duplicates from
    :return final_list: a `list` with unique (artist-track) sets
    """
    # Remove duplicate sets from track_and_artist_list
    final_list = list(set([index for index in track_and_artist_raw_list]))
    return final_list



# Load the streaming history json file
try:
    with open('/home/administrateur/Downloads/my_spotify_data/MyData/StreamingHistory1.json', 'r') as json_file:
        streaming_history_load = json.load(json_file)   # streaming_history_load -> list
except Exception as ex:
    print(f"Error: {str(ex)}")
finally:
    json_file.close()

track_and_artist_raw_list = populate_raw_list(streaming_history_load)
track_artist_final_list = remove_duplicate_items(track_and_artist_raw_list)

