from typing import List, Optional, Sequence, Set, Tuple
from .avltree import AVLTree, AVLNode

class IntervalNode():
    def __init__(self, low: float, high: float, data:any) -> None:
        self.low = low
        self.high = high
        self.max = high
        self.data = AVLTree()
        self.data.insert(high, data)
    
    def add_interval(self, high, data):
        self.data.insert(high, data)
        if high > self.high:
            self.max = high

    def __repr__(self) -> str:
        string = f'[{self.low}, {self.high}], max = {self.max}'
        return string

class IntervalTree:
    ''' Interval Tree implementation using AVL Tree '''
    def __init__(self, starting_sequence: Optional[Sequence[Tuple[float, float, any]]]=None) -> None:
        self.tree=AVLTree()
        
        if starting_sequence is not None:
            for low, high, data in starting_sequence:
                self.insert(low, high, data)
    
    def insert(self, low: float, high: float, data:any) -> None:
        '''
        Insert an interval into the tree

        Args:
        low: float: lower bound of the interval
        high: float: upper bound of the interval
        data: any: data to be stored in the interval

        Returns:
        None
        '''
        
        def _insert(node:AVLNode, low: float, high: float, data:any) -> AVLNode | None:
            if node is None:
                return AVLNode(low, IntervalNode(low, high, data))
            if node.key > low:
                node.left = _insert(node.left, low, high, data)
            elif node.key == low:
                node.value.add_interval(high, data)
                return node
            else:
                node.right = _insert(node.right, low, high, data)
            
            node.value.max = max(node.value.max, high)
            node.height = 1 + max(self.tree._height(node.left), self.tree._height(node.right))
            node=self.tree._balance_tree(node)
            return node
        
        self.tree._root = _insert(self.tree._root, low, high, data)
        self.tree._size += 1
    
    def delete_interval(self, low, high):
        node=self.tree._root
        while node is not None:
            if node.key > low:
                node = node.left
            elif node.key < low:
                node = node.right
            else:
                if node.value.data.size == 1:
                    self.tree.delete(node.key)
                else:
                    node.value.data.delete(high)
                break

    def search(self, q) -> Set:
        result = set()
        node : AVLNode = self.tree._root     #we want to find nodes that contain the value: key <= value <= high
        print(self.tree)
        while node is not None:
            if node.key <= q:
                if node.value.high >= q:
                    for item in node.value.data.values():
                        result.add(item)
                    node = node.left
                else: #node.value.high < q, so q is in the right subtree
                    node = node.right

            else: #node.key > q, so q is in the left subtree, but we need to check if the left subtree has any nodes that have less than q
                if node.left is not None and node.left.value.max >= q:
                    node = None #break loop
                else:
                    node = node.right
        return result
    
    def range_search(self, low, high) -> Set:
        result = set()
        low_search = self.search(low)
        high_search = self.search(high)
        
        for item in low_search:
            result.add(item)
        for item in high_search:
            result.add(item)

        return result



    
    
            