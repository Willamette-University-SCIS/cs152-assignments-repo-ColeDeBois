from abc import abstractmethod
from linked_list import LinkedList
from emoji import emojize
from random import randrange
from copy import deepcopy

class Dance_Floor(LinkedList):
    def __init__(self) -> None:
        super().__init__()
        self._dancers=[monkey(),beaver(),llama(),mammoth(),badger(),snake(),honeybee()]
        self._dances=['boogie','dougie','spinning top','sprinkler','white girl dance', 'twerk']
        for i in self._dancers:
            self.append(i)
    def next_round(self,dancer,rdx:int):
        if rdx == 1:
            self.boogie(dancer)
        elif rdx == 2:
            self.dougie(dancer)
        elif rdx == 3:
            self.spinning_top(dancer)
        elif rdx == 4:
            self.sprinkler(dancer)
        elif rdx == 5:
            self.white_girl_dance(dancer)
        elif rdx == 6:
            self.twerk(dancer)
    @property
    def dances_list(self):
        return self._dances
    @property
    def dancer_list(self):
        return self._dancers
    
    def __str__(self):
        string=''
        for idx,item in enumerate(self):
            string+=' '+str(item)
            if idx % (len(self.dancer_list) + 3) == 0 and idx != 0:
                string+=' \n'
        return string

    def boogie(self,dancer):
        '''Dance Number 1 - the new dancer becomes the first dancer in the line'''
        self.prepend(dancer)

    def dougie(self, dancer):
        '''Dance Number 2 - the new dancer becomes the last dancer in the line. '''
        self.append(dancer)

    def spinning_top(self,dancer):
        '''Dance Number 3 - the new dancer joins the line at a random position X, where X <= length of the line.'''
        node_before=self.head
        for X in range(randrange(len(self))):
            node_before=node_before.next
        item=node_before.item
        self.insert_before(item,dancer)

    def sprinkler(self,dancer):
        '''Dance Number 4 - remove the first matching dancer from the line and then add the new dancer to the end of the line.'''
        self.extract(dancer)
        self.append(dancer)

    def white_girl_dance(self, dancer):
        '''Dance Number 5 - take the new dancer and generate two more matching dancers. 
        Place one dancer at the front of the line, one dancer in the middle of the line, and the other dancer at the end of the line.'''
        
        front_dancer=deepcopy(dancer)
        back_dancer=deepcopy(dancer)
        self.prepend(front_dancer)
        self.append(back_dancer)
        
        node_before=self.head
        for X in range(len(self) // 2):
            node_before=node_before.next
        item=node_before.item
        self.insert_before(item,dancer)

    def twerk(self, dancer):
        '''Dance Number 6 - Add the dancer to the front of the line, then add one of each dancer type to the end of the line.'''
        self.prepend(dancer)
        for dncer in self.dancer_list:
            if not isinstance(dncer, type(dancer)):
                self.append(dncer)
    

class Dancer:
    def __init__(self) -> None:
        string=str(type(self))
        start=string.find('dancers.') + len('dancers.')
        self._name=string[start:-2]

        self.fav_song=None
    def __str__(self) -> str:
        return emojize(':'+self.name+':')
    @property
    def music(self) -> str:
        return self.fav_song
    @property
    def name(self):
        return self._name
    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name

    def __repr__(self) -> str:
        return str(self)
        

class monkey(Dancer):
    '''number one dancer'''
    def __init__(self) -> None:
        super().__init__()
        self.fav_song='DK rap - N64'
    
class beaver(Dancer):
    '''number two dancer'''
    def __init__(self) -> None:
        super().__init__()
        self.fav_song="What Do You Mean? - Justin Bieber"
    
class llama(Dancer):
    def __init__(self) -> None:
        super().__init__()
        self.fav_song="Peruvian 70s Rock"
    
class mammoth(Dancer):
    def __init__(self) -> None:
        super().__init__()
        self.fav_song="Ice Ice Baby - Vanilla Ice"

class badger(Dancer):
    def __init__(self) -> None:
        super().__init__()
        self.fav_song="Secret Tunnel - Nomad Lovers"
    
class honeybee(Dancer):
    def __init__(self) -> None:
        super().__init__()
        self.fav_song='Imma Be - Black Eyed Peas'

class snake(Dancer):
    def __init__(self) -> None:
        super().__init__()
        self.fav_song="Anaconda - Nicki Minaj"





        



