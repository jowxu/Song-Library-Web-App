from flask import Flask
from flask import render_template
from flask import request
from song_library import Song_Library
from song import Song

song_library = Song_Library()
song_library.transfer_songs('lastfm_subset')

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def home():
    """Home page of the song finder website.
    """
    categories = ['By Min # of Songs', 'By Tag', 'By Artist']
    query = {}
    search = ''
    #takes the user selected category and what they inputted in the search bar
    search_category = request.args.get('categories')
    search = request.args.get('search')

    if ((search_category and len(search_category) > 0)
    and (search and len(search) > 0)):
        if search_category == 'By Artist':
            #Search by artist feature
            try:
                result = song_library.search_by_artist(search)
                for key in result:
                    items = []
                    for item in result[key]:
                        items.append((item.title, item.track_id))
                    query[key] = items
            except:
                pass
        elif search_category == 'By Tag':
            #search by tag feature
            try:
                result = song_library.search_by_tag(search)
                for key in result:
                    items = []
                    for item in result[key]:
                        items.append((f'{item.title} by {item.artist}', item.track_id))
                    query[key] = items
            except:
                pass
        elif search_category == 'By Min # of Songs':
            #searching all artists that have a minimum of n songs
            try:
                result = song_library.get_artists_more_than_n(search)
                for key in result:
                    items = []
                    for item in result[key]:
                        items.append((item.title, item.track_id))
                    query[key] = items
            except:
                pass
    return render_template('home.html', query = query, search = search, search_category = search_category, popular_tags = song_library.get_popular_tags(), categories = categories)

@app.route('/<id>')

def song(id):
    """Webpage for specific songs that contain information.
    """
    track_id = id
    song = song_library.all_songs[track_id]
    title = song_library.all_songs[track_id].title
    artist = song_library.all_songs[track_id].artist
    tags = song_library.all_songs[track_id].tags
    similars = []
    for similar in song_library.all_songs[track_id].similars:
        if similar in song_library.all_songs:
            similars.append((similar, song_library.all_songs[similar].title, song_library.all_songs[similar].artist))
    return render_template('song.html', track_id = track_id, title = title, artist = artist, tags = tags, similars = similars, song = song)