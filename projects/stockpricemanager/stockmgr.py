from dataclasses import dataclass
from typing import List, Optional, Set, Tuple
from datastructures.intervaltree import IntervalTree

@dataclass
class Stock:
    Symbol: str
    Name: str
    low: float
    high: float

    def __str__(self) -> str:
        return f'{self.Symbol}: {self.Name}, Price: ${self.low}-${self.high}'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other: 'Stock') -> bool:
        return self.Symbol == other.Symbol 
    
    def __hash__(self) -> int:
        return hash(self.Symbol+self.Name)
    
        



class StockPriceManager:
    '''Stores stock data and provides methods to search, add, remove and find top k stocks'''
    def __init__(self, starting_sequence: Optional[List[Tuple[str, str, float, float]]]=None) -> None:
        self.tree = IntervalTree()
        if starting_sequence is not None:
            for Symbol, Name, low, high in starting_sequence:
                low, high = float(low), float(high)
                self.add_stock(Symbol, Name, low, high)
    
    def stocks_from_csv(self,file_path: str) -> None:
        '''
        Create a StockPriceManager object from a csv file

        Args:
        file_path: str: path to the csv file

        Returns:
        StockPriceManager: StockPriceManager object
        '''
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('Stock') or line.isspace():
                    continue
                Symbol, Name, low, high, date = line.strip().split(',')
                low, high = float(low), float(high)
                self.add_stock(Symbol, Name, low, high)

                
        
    def add_stock(self, Symbol: str, Name: str, low: float, high: float) -> None:
        '''
        Add a stock to the market with the given price range, if stock already exists, update the price range

        Args:
        Symbol: str: stock symbol
        Name: str: stock name
        low: float: lower bound of the price range
        high: float: upper bound of the price range

        Returns:
        None
        '''
        stock = self.search_by_symbol(Symbol)
        if stock is not None:
            self.remove_stock(Symbol)
        self.tree.insert(low, high, Stock(Symbol, Name, low, high))
    
    def search_by_symbol(self, Symbol: str) -> Stock | None:
        '''
        Given a stock symbol, return the stock, if not found return None

        Args:
        Symbol: str: stock symbol

        Returns:
        Stock: stock object
        '''
        inodes = self.tree.tree.values()
        for inode in inodes:
            for stock in inode.data.values():
                if stock.Symbol == Symbol:
                    return stock
    
    def remove_stock(self, Symbol: str) -> None:
        '''
        Given a stock symbol, remove the stock from the market

        Args:
        Symbol: str: stock symbol
        '''
        stock = self.search_by_symbol(Symbol)
        self.tree.delete_interval(stock.low, stock.high)

    def range_search(self, low, high) -> Set[Stock]:
        '''
        Find all stocks that have a price range that overlaps with the given range

        Args:
        low: float: lower bound of the range
        high: float: upper bound of the range

        Returns:
        Set[Stock]: set of stocks
        '''
        return self.tree.range_search(low, high)
    
    def find_top_k(self, k: int, Ascending:Optional[bool]=False) -> List[Stock]:
        '''
        Find the highest k stocks in the market based on low price

        Args:
        k: int: number of stocks to return
        Ascending: Optional bool: if True, return the lowest k stocks, else return the highest k stocks

        Returns:
        List[Stock]: list of stocks
        '''
        if Ascending:
            keys=self.tree.tree.inorder()[-k:]
        else:
            keys=self.tree.tree.inorder()[:k]
        stocks = []
        for key in keys:
            inode=self.tree.tree.search(key)
            for stock in inode.data.values():
                stocks.append(stock)
                if len(stocks) == k:
                    return stocks
        return stocks

        


        
    
    