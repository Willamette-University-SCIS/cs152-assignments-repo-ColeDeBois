from dataclasses import dataclass #for Song and Playlist
from datastructures.linked_list import LinkedList #for songs in playlist
from datastructures.list_queue import ListQueue as Queue #for shuffling
import time #for playing songs with delay between them
import random #for shuffling   

@dataclass
class Song:
    '''Class to represent a song in the library. The song has the following attributes:'''
    id: int
    title: str
    artist: str
    album: str
    duration: int
    plays: int = 0

    def __eq__(self, other) -> bool:
        '''songs are equal if they have the same title, artist, album, and duration. Id and plays are not considered.'''
        if self.title == other.title:
            if self.artist == other.artist:
                if self.album == other.album:
                    if self.duration == other.duration:
                        return True
        return False
    
    def __str__(self):
        return f'{self.id}, {self.title}, {self.artist}, {self.album}, {self.duration} seconds, {self.plays}'
    
@dataclass
class Playlist:
    ''' A playlist is a collection of orderd songs ids'''
    name: str
    songs = LinkedList()
    

class BBLibrary:
    '''Class to represent a music library.'''
    def __init__(self) -> None:
        self._songs = {}
        self._playlists = {}
        self._total: int = 0

    def import_music_library(self, filename: str) -> None:
        ''' Import music library from a CSV file. The CSV file will have the following format: 
        Title, Artist, Album, Duration (in seconds)
        '''
        fh = 'final_exam/'+filename+'.csv'
        with open(fh, 'r') as file:
            line_no=0
            for line in file:
                if line != '' and line_no != 0:
                    song = line.strip().split(',')
                    song = Song(id=self._total, title=song[0], artist=song[1], album=song[2], duration=song[3])
                    self._songs[song.id]=song
                    self._total += 1
                line_no += 1
    
    def add_song_to_library(self, title: str, artist: str, album: str, duration_in_seconds: int) -> None:
        ''' Add a song to the library. The song is represented by its title, artist, album, and duration. The id is automatically assigned.'''
        song = Song(id=self._total, title=title, artist=artist, album=album, duration=duration_in_seconds)
        self._songs[song.id]=song
        self._total += 1
      
    def display_library(self) -> None:
        ''' Display the library in the following format:
        ID, Title, Artist, Album, Duration, Plays
        '''
        print('Library:')
        print('ID, Title, Artist, Album, Duration, Plays')
        for i in range(self._total):
            print(self._songs[i])
        
    def create_playlist(self, name: str) -> None:
        ''' Create a playlist with the given name and songs. The songs are represented by their ids.'''
        playlist = Playlist(name)
        self._playlists[name] = playlist
    
    def add_song_to_playlist(self, playlist_name: str, song_ids: list[int] | int) -> None:
        ''' Add a song to a playlist. The song is represented by its id.'''
        playlist=self._playlists[playlist_name]
        if isinstance(song_ids, int):
            playlist.songs.append(song_ids)
        else:
            for id in song_ids:
                playlist.songs.append(id)
        
    def play_songs(self, playlist_name: str | None = None) -> None:
        ''' Play the songs in the playlist (waiting a second between songs). 
            If no playlist is provided, play all songs in the library.'''
        if playlist_name is None:
            ids=self._songs.keys()
        else:
            ids=self._playlists[playlist_name].songs
        for id in ids:
            song=self._songs[id]
            print(f'Playing {song}')
            song.plays += 1
            time.sleep(1)

    def shuffle_play(self, playlist_name: str | None = None) -> None:
        '''operates the same as play_songs but shuffles the songs before playing them.'''
        if playlist_name is None:
            ids=self._songs.keys()
        else:
            ids=self._playlists[playlist_name].songs
        
        #shuffle the ids
        ids=list(ids)   
        random.shuffle(ids)

        for id in ids:
            song=self._songs[id]
            print(f'Playing {song}')
            song.plays += 1
            time.sleep(1)
    
    def search(self, search_criteria:str, playlist_name: str | None = None) -> None:
        ''' Search for songs in the library or playlist that match the search criteria. Songs that match are printed to the terminal.'''
        if playlist_name is None:
            ids=self._songs.keys()
        else:
            ids=self._playlists[playlist_name].songs
        for id in ids:
            song=self._songs[id]
            if search_criteria in song.title or search_criteria in song.artist:
                print(song)


    def __repr__(self) -> str:
        return f'BBLibrary with {self._total} songs.'
    

