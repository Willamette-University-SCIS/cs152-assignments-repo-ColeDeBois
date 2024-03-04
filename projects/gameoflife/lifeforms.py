from abc import abstractmethod


class Lifeform:
    def __init__(self, is_alive:bool, symbol:str):
        pass
        self._is_alive=is_alive
        self._symbol=symbol
    @property
    def alive(self) -> bool:
        return self._is_alive
    @alive.setter
    def alive(self, is_alive:bool):
        self._is_alive = is_alive

    @property
    def symbol(self) -> str:
        return self._symbol
    
    @symbol.setter
    def symbol(self, new_sym):
        self._symbol=new_sym

    @abstractmethod
    def evolve(self,no_neighbors) -> None:
        pass
    
    def __str__(self) -> str:
        if self.alive:
            return self.symbol
        else:
            return ' '
    
    def __eq__(self, __o: object) -> bool:
        if type(__o) == type(self):
            if self.alive == __o.alive and self.symbol == __o.symbol:
                return True
        return False

    def __ne__(self, __o: object) -> bool:
        return not self==__o
        

class Bacteria(Lifeform):
    def __init__(self, is_alive:bool) -> None:
        super().__init__(is_alive,'X')

    def evolve(self, no_neighbors) -> None:
        if no_neighbors < 2:
            self.alive = False
        elif no_neighbors == 2:
            pass
        elif no_neighbors == 3:
            self.alive = True
        elif no_neighbors > 3:
            self.alive = False

    
        