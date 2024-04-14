from datastructures.hash_map import HashMap


class Compressor:
    def __init__(self, storage_handle:str='disk_storage' ) -> None:
        self._storage_h = storage_handle+'.txt'
        with open('projects/lyricscompressor/'+self._storage_h, 'r') as f:
            line=f.readline()
            if line == '':
                self._disk_storage = None
            else:
                self._disk_storage = line.strip('\n')
        self._stored = HashMap(100)
        self._input_h = None
        
    def compress(self,file_handle:str) -> None:
        '''
        compresses the lyrics in the file_handle into memory
        Caution! This method will overwrite any lyrics currently stored in memory
        '''
        self._input_h= 'projects/lyricscompressor/'+ file_handle + '.txt'
        fh = self._input_h
        with open(fh, 'r') as f:
            lines=f.readlines()
        hash_map = HashMap(len(lines)*7)
        hash_map['\n']=[]
        word_count = 1
        for lnum, line in enumerate(lines):
            if line == '\n':
                hash_map['\n'].append(word_count)
                word_count+=1
            else:
                line=line.split(' ')
                for wnum,word in enumerate(line):
                    if '\n' == word[-1]:
                        word = word[:-1]
                        if word in hash_map:
                            hash_map[word].append(-word_count)
                        else:
                            hash_map[word] = [-word_count]
                    else:
                        if word in hash_map:
                            hash_map[word].append(word_count)
                        else:
                            hash_map[word] = [word_count]
                    word_count+=1
        self._stored = hash_map

    def decompress(self, file_handle:str=None) -> str | None:
        '''takes the lyrics stored in memory and decompresses them, 
        returning the decompressed lyrics as a string or writing them to a file if to_file is True'''
        lyrics = ''
        place = 1
        while self._stored.keys() != []:
            for key in self._stored:
                key_places=self._stored[key]
                if place in key_places:
                    key_places.remove(place)
                    lyrics += ' '+key
                    place += 1
                elif -place in key_places:
                    key_places.remove(-place)
                    lyrics += ' '+key+'\n'
                    place += 1
                if key_places == []:
                    del self._stored[key]
        if file_handle != None:
            self.write_to_file(lyrics, file_handle+'.txt')
        else:
            return lyrics
        

    def word_positions(self) -> str:
        '''returns a string of the word positions in the lyrics stored in memory, meant to be printed to the console'''
        string='Word  Positions\n' + '-'*15+'\n'
        for key in self._stored:
            if key != '\n':
                string += key+': '+str(self._stored[key]).strip(',\n[]')+'\n'
        return string
    
    def clear_storage(self) -> None:
        '''clears out the disk storage'''
        self.write_to_file('', self._storage_h)
        self._disk_storage = None

    def pop_storage(self) -> None:
        '''clears out the disk storage and reads the contents into memory'''
        with open('projects/lyricscompressor/'+self._storage_h, 'r') as f:
            lines=f.readlines()
        for num,line in enumerate(lines):
            if num == 0:
                self._disk_storage = line.strip('\n,')
            else:
                colon = line.index(':')
                word = line[:colon]
                if word == '\\n':
                    word = '\n'
                positions = line[colon+1:].strip('\n').split(',')
                self._stored[word] = [int(pos) for pos in positions]
        self.clear_storage()

    def store_long_term(self, song_name:str) -> None:
        '''takes the current lyrics stored in memory and writes them to disk storage'''
        string=song_name+'\n'
        for key in self._stored:
            if key == '\n':
                string += '\\n'+': '+str(self._stored[key]).strip(',\n[]')+'\n'
            else:
                string += key+': '+str(self._stored[key]).strip(',\n[]')+'\n'
        self.write_to_file(string, self._storage_h)
        self._disk_storage = song_name

        
    @property
    def has_stored_to_disk(self) -> bool:
        '''returns True if a song is stored in disk storage, False otherwise'''
        return self._disk_storage != None
    
    @property
    def disk_storage(self) -> str:
        '''the name of the song stored in disk storage'''
        return self._disk_storage

    @staticmethod
    def write_to_file(content:str, file_handle:str) -> None:
        '''general method to write to a file, file_handle must include the formatting like .txt or .csv'''
        with open('projects/lyricscompressor/'+file_handle, 'w') as f:
            f.write(content)

