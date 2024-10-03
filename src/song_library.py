#Joel
#song library class

import os
import json
from song import Song

class Song_Library:
    def __init__(self):
        """Constructor that creates dictionaries
        for all song objects, one by artists,
        and one by tags.
        """
        self.all_songs = {}
        self.by_artist = {}
        self.by_tags = {}
    
    def add_song(self, song):
        """Input: song object adds song to all_songs
        and by_artist and by_tags if the track_id is new.
        param song: Song object
        """
        if song.track_id not in self.all_songs:
            self.all_songs[song.track_id] = song
            if song.artist not in self.by_artist:
                self.by_artist[song.artist] = [song]
            else:
                self.by_artist[song.artist].append(song)
            if song.tags != []:
                for tag in song.tags:
                    if tag not in self.by_tags:
                        self.by_tags[tag] = [song]
                    else:
                        self.by_tags[tag].append(song)

    def get_all_songs(self):
        return self.all_songs

    def get_by_artist(self):
        return self.by_artist

    def get_by_tags(self):
        return self.by_tags

    def transfer_songs(self, lastfm_subset):
        """
        transfers all the songs in the JSON file to
        a song library data structure.
        param song_library: the song library object
        param lastfm_subset: the top level folder containing all the json songs, or just one json file
        """
        if lastfm_subset.endswith('.json'):
            with open(lastfm_subset) as song_data:
                    json_song = json.load(song_data)
                    if json_song['track_id'] not in self.all_songs:
                        song = self.convert_song(json_song)
                        self.add_song(song)
        else:
            for dirpath, dirnames, filenames in os.walk(lastfm_subset): #https://docs.python.org/3/library/os.html
                for filename in filenames:
                    json_path = os.path.join(dirpath, filename)
                    with open(json_path) as song_data:
                        json_song = json.load(song_data)
                        if json_song['track_id'] not in self.all_songs:
                            song = self.convert_song(json_song)
                            self.add_song(song)

    def convert_song(self, json_song):
        """converts the json song into a
        song object.
        param json_song: json song object
        returns: python song object
        """
        track_id = json_song['track_id']
        title = json_song['title']
        artist = json_song['artist']
        tags = []
        similars = []
        if len(json_song['tags']) > 0:
            for tag in json_song['tags']:
                if tag[0] not in tags:
                    tags.append(tag[0])
        if len(json_song['similars']) > 0:
            for similar in json_song['similars']:
                if similar[0] not in similars:
                    similars.append(similar[0])
        song = Song(track_id, title, artist , tags, similars)
        return song

    def search_by_artist(self, artist: str) -> str:
        """Lists all the songs created by artist inputted by user.
        artist: artist name requested by user
        returns: dictionary of artist and all the songs the artist has
        """
        if artist not in self.by_artist:
            raise Exception('Artist does not exist in Song Library.')
        result = {artist: self.by_artist[artist]}
        return result

    def search_by_tag(self, tag: str):
        """searches by tag dictionary and finds all songs with user
        inputted tag and returns a string of all songs that have tag.
        param tag: the tag the user inputted
        """
        if tag not in self.by_tags:
            raise Exception('Tag does not exist in Song Library.')
        result = {tag: self.by_tags[tag]}
        return result

    def get_popular_tags(self) -> dict:
        """Takes the song_library by tags and scans the length for the top 10
        most popular tags.
        returns: a dictionary containing the top 10 most popular tags and how many songs are in each of them
        """
        tag_sizes = {}
        for tag in self.by_tags:
            tag_sizes[tag] = len(self.by_tags[tag])
        popular_tags = {}
        if len(self.by_tags) <= 10:
            tag_sizes = sorted(tag_sizes.items(), key = lambda x:x[1], reverse = True) #https://www.geeksforgeeks.org/different-ways-of-sorting-dictionary-by-values-and-reverse-sorting-by-values/
            popular_tags = dict(tag_sizes)
        else:
            for i in range(10):
                largest_tag = max(tag_sizes, key = tag_sizes.get) #https://www.geeksforgeeks.org/python-n-largest-values-in-dictionary/
                popular_tags[largest_tag] = tag_sizes[largest_tag]
                del tag_sizes[largest_tag]
        del tag_sizes
        return popular_tags

    def get_artists_more_than_n(self, n: str) -> dict:
        """Takes the by artist dictionary and scans for all
        the artists that have n or more songs and returns a dictionary
        containing all artists that fit the criteria.
        param n: floor for number of songs
        returns: a dictionary containing all artists that have n or more songs and the songs as the value.
        """
        n = int(n)
        if n < 0:
            raise Exception('Minimum # of songs from an artist must be a non-negative integer.')
        n_songs_artists = {}
        for artist in self.by_artist:
            if len(self.by_artist[artist]) >= n:
                n_songs_artists[artist] = self.by_artist[artist]
        return n_songs_artists