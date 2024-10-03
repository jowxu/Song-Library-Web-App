#Joel
#song library test

import unittest
import src
import song_library
import song
from song_library import Song_Library
from song import Song

class song_library_test(unittest.TestCase):
    def test_constructor(self):
        """Tests if the constructor creates 3 empty dictionaries.
        """
        song_library = Song_Library()
        self.assertEqual(song_library.all_songs, {})
        self.assertEqual(song_library.by_artist, {})
        self.assertEqual(song_library.by_tags, {})

    def test_add_new_song(self):
        """tests if the song library successfully creates a singular instance of the song
        and is placed correctly in all dictionaries.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        self.assertEqual(library.all_songs[song.track_id].track_id, song.track_id)
        self.assertEqual(library.by_artist[song.artist][0].artist, song.artist)
        self.assertEqual(library.by_tags[song.tags[0]][0].tags, song.tags)
        self.assertEqual(library.by_tags[song.tags[1]][0].tags, song.tags)

    def test_add_existing_song(self):
        """Tests that the library will not add a song with a duplicate
        track ID.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('AEDO', 'Backlights', 'Adon', ['pops', 'rocks'])
        library.add_song(song2)
        self.assertEqual(len(library.all_songs), 1)
        self.assertEqual(len(library.by_artist), 1)
        self.assertEqual(len(library.by_artist[song.artist]), 1)
        self.assertEqual(len(library.by_tags), 2)
        self.assertEqual(len(library.by_tags[song.tags[0]]), 1)
        self.assertEqual(len(library.by_tags[song.tags[1]]), 1)

    def test_add_2_songs_sharing_1_tag(self):
        """Tests that the library successfully adds 2 songs, sharing one duplicate tag.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'TK', ['rock', 'metal'])
        library.add_song(song2)
        self.assertEqual(len(library.all_songs), 2)
        self.assertEqual(len(library.by_artist), 2)
        self.assertEqual(len(library.by_tags), 3)
        self.assertEqual(len(library.by_tags[song.tags[0]]), 1)
        self.assertEqual(len(library.by_tags[song.tags[1]]), 2)
        self.assertEqual(len(library.by_tags[song2.tags[1]]), 1)

    def test_add_2_songs_sharing_1_artist(self):
        """Tests that the library successfully adds 2 songs, sharing an artist.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        self.assertEqual(len(library.all_songs), 2)
        self.assertEqual(len(library.by_artist), 1)
        self.assertEqual(len(library.by_artist[song.artist]), 2)
        self.assertEqual(len(library.by_tags), 3)

    def test_search_by_artist_2_songs(self):
        """tests search_by_artist when adding 2 songs to 1 artist
        and 1 song to another artist and searching with the artist with 2 songs.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'tag2'])
        library.add_song(song3)
        ado = library.search_by_artist('Ado')
        self.assertEqual(len(ado), 1)
        self.assertEqual(len(ado['Ado']), 2)
        self.assertEqual(ado['Ado'], [song, song2])

    def test_search_by_artist_dne(self):
        """tests for exception when searching with an artist
        that does not exist.
        """
        library = Song_Library()
        with self.assertRaises(Exception):
            ado = library.search_by_artist('Ado')

    def test_search_by_tag_3_songs(self):
        """tests search_by_tag and checks if 3 songs successfully added
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        tag = library.search_by_tag('rock')
        self.assertEqual(len(tag), 1)
        self.assertEqual(len(tag['rock']), 3)
        self.assertEqual(tag['rock'], [song, song2, song3])
        tag = library.search_by_tag('pop')
        self.assertEqual(len(tag), 1)
        self.assertEqual(len(tag['pop']), 1)
        self.assertEqual(tag['pop'], [song])

    def test_search_by_tag_dne(self):
        """tests for exception raised when searching a tag that does not exist.
        """
        library = Song_Library()
        with self.assertRaises(Exception):
            tag = library.search_by_tag('rock')

    def test_get_popular_tags_11_tags(self):
        """tests for getting 10 most popular tags with 11 tags created.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        song4 = Song('id1', 'song4', 'artist1', ['tag2', 'rock', 'metal'])
        library.add_song(song4)
        song5 = Song('id2', 'song5', 'artist1', ['tag3', 'rock', 'tag2', 'metal'])
        library.add_song(song5)
        song6 = Song('id3', 'song6', 'artist1', ['tag4', 'rock', 'tag1'])
        library.add_song(song6)
        song7 = Song('id4', 'song7', 'artist1', ['tag5', 'rock', 'tag3'])
        library.add_song(song7)
        song8 = Song('id5', 'song8', 'artist1', ['tag6', 'rock', 'tag4'])
        library.add_song(song8)
        song9 = Song('id6', 'song9', 'artist1', ['tag7', 'rock', 'pop', 'tag8'])
        library.add_song(song9)
        popular_tags = library.get_popular_tags()
        self.assertEqual(len(popular_tags), 10)
        self.assertEqual(popular_tags['rock'], 9)
        self.assertEqual(popular_tags['pop'], 2)

    def test_get_popular_tags_6_tags(self):
        """tests fo get popular tags when only 6 tags exist
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        song4 = Song('id1', 'song4', 'artist1', ['tag2', 'rock', 'metal'])
        library.add_song(song4)
        song5 = Song('id2', 'song5', 'artist1', ['tag3', 'rock', 'tag2', 'metal'])
        library.add_song(song5)
        popular_tags = library.get_popular_tags()
        self.assertEqual(len(popular_tags), 6)
        self.assertEqual(popular_tags['rock'], 5)
        self.assertEqual(popular_tags['pop'], 1)

    def test_get_artist_n_songs(self):
        """tests get artists with n songs or more method.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        song4 = Song('id1', 'song4', 'artist1', ['tag2', 'rock', 'metal'])
        library.add_song(song4)
        song5 = Song('id2', 'song5', 'artist1', ['tag3', 'rock', 'tag2', 'metal'])
        library.add_song(song5)
        two = library.get_artists_more_than_n('2')
        self.assertEqual(len(two), 2)
        self.assertEqual(two['Ado'], [song, song2])
        self.assertEqual(two['artist1'], [song3, song4, song5])
        three = library.get_artists_more_than_n('3')
        self.assertEqual(len(three), 1)
        self.assertEqual(three['artist1'], [song3, song4, song5])

    def test_get_artist_n_songs_value_error(self):
        """tests that inputting a string that isn't an integer results in a value error.
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        song4 = Song('id1', 'song4', 'artist1', ['tag2', 'rock', 'metal'])
        library.add_song(song4)
        song5 = Song('id2', 'song5', 'artist1', ['tag3', 'rock', 'tag2', 'metal'])
        library.add_song(song5)
        with self.assertRaises(ValueError):
            two = library.get_artists_more_than_n('woah')

    def test_get_artist_n_songs_exception(self):
        """tests that entering a negative integer raises an exception
        """
        library = Song_Library()
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        library.add_song(song)
        song2 = Song('HAHA', 'Unravel', 'Ado', ['rock', 'metal'])
        library.add_song(song2)
        song3 = Song('WOAH', 'song3', 'artist1', ['tag1', 'rock'])
        library.add_song(song3)
        song4 = Song('id1', 'song4', 'artist1', ['tag2', 'rock', 'metal'])
        library.add_song(song4)
        song5 = Song('id2', 'song5', 'artist1', ['tag3', 'rock', 'tag2', 'metal'])
        library.add_song(song5)
        with self.assertRaises(Exception):
            two = library.get_artists_more_than_n('-4')

    def test_transfer_songs(self):
        """tests the transfer method.
        """
        library = Song_Library()
        library.transfer_songs('lastfm_subset\\A\\A\\A')
        self.assertEqual(len(library.all_songs), 11)

    def test_transfer_1_song_json(self):
        """tests the transfer method for when theres only one json file.
        """
        library = Song_Library()
        library.transfer_songs('lastfm_subset\\A\\A\\A\\TRAAAAW128F429D538.json')
        self.assertEqual(len(library.all_songs), 1)

def main():
    unittest.main()

if __name__ == '__main__':
    main()