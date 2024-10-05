from __future__ import annotations
from typing import Sequence, Tuple
from datastructures.iavltree import *
from datastructures.list_queue import ListQueue as queue

# datastructures.avltree.AVLNode
class AVLNode(Generic[K, V]):
    def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):
        self._key = key
        self._value = value
        self._left = left
        self._right = right
        self._height = 0
    
    @property 
    def key(self) -> K:
        return self._key
    
    @key.setter
    def key(self, key: K) -> None:
        self._key = key

    @property
    def value(self) -> V: 
        return self._value
    
    @value.setter
    def value(self, value: V) -> None: 
        self._value = value
    
    @property
    def left(self) -> Optional[AVLNode]: 
        return self._left

    @left.setter
    def left(self, left: Optional[AVLNode]) -> None: 
        self._left = left

    @property
    def right(self) -> Optional[AVLNode]: 
        return self._right

    @right.setter
    def right(self, right: Optional[AVLNode]) -> None: 
        self._right = right

    @property
    def height(self) -> int: 
        return self._height
    
    @height.setter
    def height(self, height: int) -> None: 
        self._height = height

    

    def __repr__(self) -> str:
        string = f'{self._key}: {self._value} \n'
        if self._left is not None:
            string += f' -> {self._left}'
        if self._right is not None:
            string += f' -> {self._right}'
        return string

# datastructures.avltree.AVLTree
'''
to do:
- delete
- heights (likely the cause for bad ordering (ie balance factor is off bc heights are off))
'''
class AVLTree(IAVLTree[K, V], Generic[K, V]):
    def __init__(self, starting_sequence: Optional[Sequence[Tuple[K, V]]]=None) -> None:
        self._root:AVLNode = None
        self._size=0

        if starting_sequence is not None:
            for key, value in starting_sequence:
                self.insert(key, value)
    
    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0
    
    def _balance_factor(self, node:AVLNode) -> int:
        return self._height(node.left) - self._height(node.right)
    
    def _rotate_left(self, node: AVLNode) -> AVLNode: 
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        new_root.right #doesn't change

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root
    
    def _rotate_right(self, node: AVLNode) -> AVLNode:
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        new_root.left #doesn't change
        
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))
        return new_root
    
    def _balance_tree(self, node:AVLNode) -> AVLNode: 
        if self._balance_factor(node) > 1:
            if self._balance_factor(node.left) >= 0: 
                return self._rotate_right(node) # LL case
            else:
                node.left=self._rotate_left(node.left) # LR case
                return self._rotate_right(node)
        
        elif self._balance_factor(node) < -1:
            if self._balance_factor(node.right) <= 0: 
                return self._rotate_left(node) # RR case
            else: 
                node.right=self._rotate_right(node.right) # RL case
                return self._rotate_left(node)
        
        else:
            return node
                
        
    def _insert(self, node:AVLNode, key: K, value: V) -> None: 
        #base case
        if node is None:
            return AVLNode(key, value)
        
        #recursive case
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            raise ValueError("Key already exists in the tree")
        
        #bookkeeping
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node=self._balance_tree(node)
        return node

    def insert(self, key: K, value: V) -> None:
        self._root=self._insert(self._root, key, value)
        self._size+=1
        
    
    def search(self, key: K) -> V | None: 
        node = self._root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None

    def delete(self, key: K) -> None: 
        self._root = self._delete(self._root, key)

    def _delete(self, node: Optional[AVLNode], key: K) -> Optional[AVLNode]:     
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            #case 1: no children: just get rid of the node
            if node.left is None and node.right is None:
                return None 
            #case 2: one child 
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #case 3: two children
            else:
                temp = node.right
                while temp.left is not None:
                    temp = temp.left #find the left most node in the right subtree
                node.key, node.value = temp.key, temp.value #transfer the key and value from successor
                node.right = self._delete(node.right, temp.key) #delete the successor
        #bookkeeping
        if node is not None:
            node.height = 1 + max(self._height(node.left), self._height(node.right))
            return self._balance_tree(node)
        
        

            
    
    def inorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        def _inorder(current, keys):
            if current is not None:
                _inorder(current.left, keys)
                keys.append(current.key)
                _inorder(current.right, keys)
        keys = []
        _inorder(self._root, keys)
        return keys
        
    def preorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        def _preorder(current, keys):
            if current is not None:
                keys.append(current.key)
                _preorder(current.left, keys)
                _preorder(current.right, keys)
        keys = []
        _preorder(self._root, keys)
        return keys

    def postorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        def _postorder(current, keys):
            if current is not None:
                _postorder(current.left, keys)
                _postorder(current.right, keys)
                keys.append(current.key)
        keys = []
        _postorder(self._root, keys)
        return keys

    def bforder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        que = queue()
        keys = []
        que.enqueue(self._root)
        while len(que) > 0:
            node = que.dequeue()
            keys.append(node.key)
            if node.left is not None:
                que.enqueue(node.left)
            if node.right is not None:
                que.enqueue(node.right)
        return keys
            
    def size(self) -> int: 
        return self._size

    def __str__(self) -> str:
        def draw_tree(node: Optional[AVLNode], level: int=0) -> None:
            if not node:
                return 
            draw_tree(node.right, level + 1)
            level_outputs.append(f'{" " * 4 * level} -> {str(node.value)}')
            draw_tree(node.left, level + 1)
        level_outputs: List[str] = []
        draw_tree(self._root)
        return '\n'.join(level_outputs)

    def __repr__(self) -> str:
        descriptions = ['Breadth First: ', 'In-order: ', 'Pre-order: ', 'Post-order: ']
        traversals = [self.bforder(), self.inorder(), self.preorder(), self.postorder()]
        return f'{"\n".join([f'{desc} {"".join(str(trav))}' for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}' 
 

    