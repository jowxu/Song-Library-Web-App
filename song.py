#Joel Xu
#Song Class

class Song:
    def __init__(self, track_id: str, title: str, artist: str, tags = None, similars = None):
        """Constructor:
        Input: track id, title, artist, and tags of song
        Creates a Song object with said properties.
        param track_id: unique track id of song
        param title: title of song
        param artist: artist of song
        param tags: list of tags of song
        """
        self.track_id = track_id
        self.title = title
        self.artist = artist
        if tags == None:
            self.tags = []
        else:
            self.tags = tags
        if similars == None:
            self.similars = []
        else:
            self.similars = similars