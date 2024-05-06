from .bblibrary import BBLibrary

lib=BBLibrary()
lib.import_music_library('songs')
lib.create_playlist('my_playlist')
lib.add_song_to_playlist('my_playlist', [0,1,2])
lib.shuffle_play('my_playlist')
lib.shuffle_play()
lib.search('Harry')