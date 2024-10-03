#Joel Xu
#Song Finder

import sys
import os
import json
from song import Song
from song_library import Song_Library

def nice_print_search_by_artist(search_by_artist) -> str:
    """takes the by searched_by_artist dictionary and returns
    a formatted string of the artist and all of the titles of their songs.
    param search_by_artist: the dictionary containing the artist and all their songs.
    returns: a formatted string with the above information
    """
    for artist in search_by_artist:
        result = f'All Songs by {artist}:\n'
        for song in search_by_artist[artist]:
            result += f'    {song.title}\n'
        result = result[:-1]
        result += '\n'
    return result

def nice_print_search_by_tag(search_by_tag) -> str:
    """takes the by searched_by_tags dictionary and returns
    a formatted string of the tag and all songs that have that tag.
    param search_by_tag: the dictionary containing the tag and all songs with the tag
    returns: formatted string with above information
    """
    for tag in search_by_tag:
        result = f'All Songs that have tag \"{tag}\":\n'
        for song in search_by_tag[tag]:
            result += f'    {song.artist} - {song.title}\n'
        result = result[:-1]
        result += '\n'
    return result

def nice_print_popular_tags(song_library):
    """prints the most popular tags, up to 10.
    param song_library: the song library object
    returns: formatted string of the most popular tags
    """
    popular_tags = song_library.get_popular_tags()
    if len(popular_tags) < 10:
        result = 'Most Popular Tags:\n'
    else:
        result = 'Top 10 Most Popular Tags:\n'
    for tag in popular_tags:
        result += f'    {tag} - {popular_tags[tag]}\n'
    return result

def nice_print_get_artists_more_than_n(song_library, n: int) -> str:
    """prints the artists that have more than
    n songs and all the songs related to them.
    param song_library: song library object
    param n: number of songs
    returns: formatted string with all artists that have at least n songs
    """
    artists_more_than_n = song_library.get_artists_more_than_n(n)
    result = f'Artists with {n} or more songs:\n'
    if len(artists_more_than_n) < 1:
        result += 'None\n'
    else:
        for artist in artists_more_than_n:
            result += f'    {artist}:\n'
            for song in artists_more_than_n[artist]:
                result += f'        {song.title}\n'
    return result

def nice_print_all_songs(song_library) -> str:
    """takes the all_songs dictionary and
    prints out all songs titles with associated artist.
    param song_library: the dictionary with all songs with the track id as the key
    """
    result = 'All Songs:\n'
    for song_id in song_library.all_songs:
        result += f'{   song_library.all_songs[song_id].artist} - {song_library.all_songs[song_id].title}\n'
    return result

def nice_print_by_artist(song_library) -> str:
    """takes the by artist dictionary and
    prints out all songs, grouped by artist with title
    param all_songs: the dictionary with all songs with the track id as the key
    returns: all songs, grouped by artist
    """
    result = 'All Songs Sorted by Artist:\n'
    for artist in song_library.by_artist:
        result += f'{artist}:\n'
        for song in song_library.by_artist[artist]:
            result += f'    {song.title}\n'
    return result

def nice_print_by_tags(song_library) -> str:
    """takes the song library and prints out all tags and songs that have
    those tags.
    param song_library: the song library object
    returns: formatted string of the by tags dictionary
    """
    result = 'All Songs Sorted by Tags:\n'
    for tag in song_library.by_tags:
        result += f'    {tag}: '
        for song in song_library.by_tags[tag]:
            result += f'        {song.artist} - {song.title}\n'
    return result

def get_user_selection() -> str:
    """Asks for the users selection of options 1 - 5.
    returns: str of an int 1-5
    """
    print('Menu:\n')
    print(f'    1 - Search by artist')
    print(f'    2 - Search by tag')
    print(f'    3 - Most popular tags')
    print(f'    4 - Artists that have n songs')
    print(f'    5 - All songs')
    inputting = True
    while inputting:
        user_input = input('Please input the corresponding number of what information you would like to access: ')
        if user_input not in ['1', '2', '3', '4', '5']:
            print('Please input an integer between 1-5.')
        else:
            inputting = False
    return user_input

def return_corresponding_info(song_library, user: str) -> str:
    """gets the user request and then gets the required inputs to access
    wanted information.
    param song_library: song library object
    param user: user input of 1-5
    returns: resulting string from the choice of the user
    """
    correct = False
    result = ''
    if user == '1':
        while not correct:
            try:
                artist = str(input('What is the artist you would like to search(or type quit to exit program)? '))
                if artist == 'exit':
                    exit()
                result = nice_print_search_by_artist(song_library.search_by_artist(artist))
                correct = True
            except Exception as ex1:
                print(ex1)
                print('Please input an artist that exists in the song library.')
    elif user == '2':
        while not correct:
            try:
                tag = str(input('What is the tag you would like to search(or type quit to exit program)? '))
                if tag == 'exit':
                    exit()
                result = nice_print_search_by_tag(song_library.search_by_tag(tag))
                correct = True
            except Exception as ex1:
                print(ex1)
                print('Please input a tag that exists in the song library.')
    elif user == '3':
        result = nice_print_popular_tags(song_library)
    elif user == '4':
        while not correct:
            try:
                n = (input('What is the number of songs? '))
                if n == 'exit':
                    exit()
                result = nice_print_get_artists_more_than_n(song_library, n)
                correct = True
            except Exception as ex1:
                print(ex1)
                print('Please input a non-negative integer.')
    elif user == '5':
        result = nice_print_all_songs(song_library)
    return result

def main():
    song_library = Song_Library()
    try:
        lastfm_subset = sys.argv[1]
    except:
        print('Please type in the command: \'song_finder.py \' and the location of the top-level lastsfm_subset directory.')
        exit()
    print('Setting up Song Library.')
    try:
        song_library.transfer_songs(lastfm_subset)
        print('Song library established.')
    except:
        print('Incorrect top-level lastsfm_subset directory.')
        exit()
    using = True
    while using:
        user_input = get_user_selection()
        print(return_corresponding_info(song_library, user_input))
        yes_or_no = False
        while not yes_or_no:
            using = str(input('Would you like to select from the menu again? ')).lower()
            if not (using == 'yes' or using == 'no'):
                print('Please input yes or no.')
            else:
                yes_or_no = True
        if using == 'no':
            using = False

if __name__ == '__main__':
    main()