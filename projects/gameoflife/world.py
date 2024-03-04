import copy
import time
from datastructures.array2d import Array2D
import random
from .lifeforms import Bacteria
from .kbhit import KBHit

class World:
    def __init__(self, size: int=10, filename: str = '') -> None:
        self._grid=self._initialize_grid(size, filename)
        self._grid_history=[]
    def _initialize_grid(self, size:int, filename:str) -> Array2D:
        if filename != '':
            return self.initalize_grid_from_file(size, filename)
        grid=Array2D(size,size)
        for row in range(size):
            for col in range(size):
                alive_state=random.choice([True,False])
                grid[row][col]=Bacteria(alive_state)
        return grid
    
    def initalize_grid_from_file(self, size, filename) -> Array2D:
        grid=Array2D(size,size)
        with open(filename,'r') as fh:
            for i,line in enumerate(fh):
                line=line.split(',')
                for j,char in enumerate(line):
                    grid[i][j]=Bacteria(char == 'X')
        return grid

    def print_current_grid(self):
        for row in self._grid:
            print(row)
        print('_'*(self._grid.dimensions[0]*3+2))

    def _get_neighbors(self,row,col):
        n_neighbors=0
        for i in range(-1,2):
            for j in range(-1,2):
                if not (i == 0 and j == 0):
                    try:
                        if self._grid[row+i][col+j].alive:
                            n_neighbors += 1
                    except IndexError:
                        pass
        return n_neighbors
            
    def progress(self):
        self.print_current_grid()

        next_gen=copy.deepcopy(self._grid)
        rows,cols=next_gen.dimensions
        for row in range(rows):
            for col in range(cols):
                n_neighbors=self._get_neighbors(row,col)
                next_gen[row][col].evolve(n_neighbors)
        if self._grid == next_gen:
            return False

        self._grid_history.append(self._grid)
        self._grid=next_gen

        return True



            
            
            

  