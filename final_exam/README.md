`I Used CoPilot During the Exam`
# Bearcat Beats

### BBLibrary class

This class is the primary class that stores the songs and playlists. It uses a dictionary (hash map) for storing so there are no duplicate songs, and to make sure that the songs will have a constant lookup time using their ids as their keys. A dictionary (hash map) is also used for playlists so that they can be easily called using constant time by name, and so that there cannot be playlists with the same name.

#### Class Methods

    import_music_library(filename: str)

add a bunch of songs into the library by passing in the name of the .csv file that contains each song by line in the format of 'Title, Artist, Album, Duration (in seconds)'.

    add_song_to_library(title: str, artist: str, album: str, duration_in_seconds: int) -> None 

allows for adding individual songs to the library.

    display_library()

will print the library to the terminal, song by song in order of addition. In the format of Id, Title, Artist, Album, Duration (seconds)

    create_playlist(playlist_name: str) -> None

creates a playlist that can be called to play a subset of the library.

    add_songs_to_playlist(playlist_name: str, songs: list[int]) -> None

allows you to add one or more songs to a given playlist.

    play_songs(playlist_name: str | None=None) -> None

allows you to play the whole library or a playlist if a name was given. The songs will be iterated through, "playing" each by printing their information and adding to their to 'plays'. There is a second wait time between "playing" each song.

    shuffle_play(playlist_name: str | None=None) -> None

allows you to play either the library or a playlist but with the order shuffled. Utilizes random.shuffle for the randomization. The linked list internal structure of playlists do make this method slightly slower than the play_songs method because it must be converted to an array-like structure to shuffle the order.

    search(search_criteria: str, playlist_name: str | None=None) -> None

allows you to enter any string and find the songs that have that substring within its title or artist. Efficiency is 
$$O(n)2O(k)$$ 
where n is the size of library and k is the ratio of the search criteria to the typical length of the artist and title.

### Song class

This class is how the information of the songs are stored, using a dataclass object. Utilizing a custom dataclass for songs allows us to give it a custom `__str__` method that can be used everytime we need to print a song to the terminal. The information is stored as such:

    id: int
    title: str
    artist: str
    album: str
    duration: int
    plays: int = 0

### Playlist class

This class is responsible for storing information needed for songs. It utilizes being a dataclass that merely stores song ids in a linked list. We're using a linked list here because of its efficiency for resizing because a playlist's size will typically be incrementally grown overtime.

    name: str
    songs: LinkedList[int]
