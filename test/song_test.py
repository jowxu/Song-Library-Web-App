#Joel Xu
#Song finder test

from song import Song
import unittest

class song_test(unittest.TestCase):
    """tests the functions of the song.py
    and its functions.
    """
    def test_constructor(self):
        """tests the song constructor.
        """
        song = Song('AEDO', 'Backlight', 'Ado', ['pop', 'rock'])
        self.assertEqual(song.track_id, 'AEDO')
        self.assertEqual(song.title, 'Backlight')
        self.assertEqual(song.artist, 'Ado')
        self.assertEqual(song.tags, ['pop', 'rock'])

    def test_no_tags(self):
        """tests the constructor has tags
        as an empty list if no tags are inputed.
        """
        song = Song('AEDO', 'Backlight', 'Ado')
        self.assertEqual(song.tags, [])

def main():
    unittest.main()

if __name__ == '__main__':
    main()