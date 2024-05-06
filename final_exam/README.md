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

## Example Outputs
    lib.play_songs(my_playlist) Output:
    Playing 0, Watermelon Sugar, Harry Styles, Fine Line, 174 seconds, 0
    Playing 1, As It Was, Harry Styles, Harry's House, 169 seconds, 0
    Playing 2, Adore You, Harry Styles, Fine Line, 201 seconds, 0


    lib.shuffle_play(my_playlist) Output:
    Playing 0, Watermelon Sugar, Harry Styles, Fine Line, 174 seconds, 1
    Playing 2, Adore You, Harry Styles, Fine Line, 201 seconds, 1
    Playing 1, As It Was, Harry Styles, Harry's House, 169 seconds, 1


    lib.search("Harry") Output:
    0, Watermelon Sugar, Harry Styles, Fine Line, 174 seconds, 2
    1, As It Was, Harry Styles, Harry's House, 169 seconds, 2
    2, Adore You, Harry Styles, Fine Line, 201 seconds, 2


    lib.search("Harry", "my_playlist") Output:
    Library:
    ID, Title, Artist, Album, Duration, Plays
    0, Watermelon Sugar, Harry Styles, Fine Line, 174 seconds, 2
    1, As It Was, Harry Styles, Harry's House, 169 seconds, 2
    2, Adore You, Harry Styles, Fine Line, 201 seconds, 2
    3, Levitating, Dua Lipa, Future Nostalgia, 203 seconds, 0
    4, Blinding Lights, The Weeknd, After Hours, 200 seconds, 0
    5, Heat Waves, Glass Animals, Dreamland, 238 seconds, 0
    6, Industry Baby, Lil Nas X, Montero, 136 seconds, 0
    7, Shivers, Ed Sheeran, =, 213 seconds, 0
    8, Bad Habits, Ed Sheeran, =, 231 seconds, 0
    9, STAY (with Justin Bieber), The Kid LAROI, Over You, 166 seconds, 0
    10, Leave The Door Open, Silk Sonic, An Evening with Silk Sonic, 256 seconds, 0
    11, Drivers License, Olivia Rodrigo, Sour, 245 seconds, 0
    12, Good 4 U, Olivia Rodrigo, Sour, 178 seconds, 0
    13, Happier Than Ever, Billie Eilish, Happier Than Ever, 299 seconds, 0
    14, Peaches (feat. Daniel Caesar & Giveon), Justin Bieber, Justice, 198 seconds, 0
    15, Montero (Call Me By Your Name), Lil Nas X, Montero, 133 seconds, 0
    16, Don't Start Now, Dua Lipa, Future Nostalgia, 183 seconds, 0
    17, Save Your Tears, The Weeknd, After Hours, 215 seconds, 0
    18, positions, Ariana Grande, positions, 168 seconds, 0
    19, 7 rings, Ariana Grande, Thank U, 180 seconds, 0
    20, Without Me, Halsey, Manic, 185 seconds, 0
    21, Someone You Loved, Lewis Capaldi, Divinely Uninspired to a Hellish Extent, 182 seconds, 0
    22, Shallow, Lady Gaga & Bradley Cooper, A Star Is Born Soundtrack, 216 seconds, 0
    23, Havana (feat. Young Thug), Camila Cabello, Camila, 212 seconds, 0
    24, Dance Monkey, Tones and I, The Kids Are Coming, 207 seconds, 0
    25, Señorita, Shawn Mendes with Camila Cabello, Shawn Mendes, 191 seconds, 0
    26, Sunflower (Spiderman: Into the Spider-Verse), Post Malone & Swae Lee, Spider-Man: Into the Spider-Verse Soundtrack, 159 seconds, 0
    27, The Box, Roddy Ricch, Please Excuse Me for Being Antisocial, 210 seconds, 0
    28, Rockstar, Post Malone, Beerbongs & Bentleys, 217 seconds, 0
    29, Old Town Road (Remix), Lil Nas X (feat. Billy Ray Cyrus), Old Town Road EP, 157 seconds, 0
