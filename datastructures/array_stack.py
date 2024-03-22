from typing import Any
from datastructures.array import Array

class ArrayStack:
    """ Class ArrayStack - representing a fixed-size stack using a 1D Array object.
        Stipulations:
        1. Must use an Array object as the internal data structure from the Array assignment.
        2. Must adhere to the docstring requirements per method, including raising
            raising appropriate exceptions where indicated.
    """

    def __init__(self, max_size: int = 0) -> None:
        """ Constructor

        Examples:
            >>> stack = ArrayStack(10)

        Args:
            max_size (int): the desired size of the stack.

        Returns:
            None
        """
        self._ar=Array(size=max_size)
        self._max_size=max_size
        self._count = 0 

    def push(self, item: Any) -> None:
        """ Push an item onto the stack.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> stack.push('cat')
            
        Args:
            item (Any): the item to enqueue.
                
        Returns:
            None

        Raises:
            IndexError: if the stack is full.
        """
        if self.full:
            raise IndexError
        self._ar[self._count]=item
        self._count+=1

    def pop(self) -> Any:
       """ Pop an item from the stack and return the item.
       
        Examples:
            >>> stack = ArrayStack(10)
            >>> stack.push('cat')
            >>> item = stack.pop()
            >>> print(item)
            cat

        Returns:
            Any: the item that is popped.

        Raises:
            IndexError: if the stack is empty.

        """
       if self.empty:
           raise IndexError
       item=self.top
       self._ar[self._count]=None
       self._count-=1
       return item

    def clear(self) -> None:
        """Clear the stack.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> stack.push('cat')
            >>> stack.clear()
            >>> print(stack.empty)
            True
                
        Returns:
            None
        """
        self._count = 0
        self._ar=Array(self.max_size)
        
    @property
    def top(self) -> Any:
        """Get the item at the top of the stack.
            
        Examples:
            >>> stack = ArrayStack(10)
            >>> stack.push('cat')
            >>> print(stack.top)
            cat
        
        Returns:
            Any: the item that is at the top of the stack.
            
        Raises:
                IndexError: if the stack is empty.
        """
        if self.empty:
            raise IndexError
        return self._ar[self._count-1]

    @property
    def max_size(self) -> int:
        """Get the maximum size of the stack.

        Examples:
            >>> stack = ArrayStack(10)
            >>> print(stack.max_size)
            10

        Returns:
            int: the max size of the stack.
        """
        return self._max_size
    
    @property
    def full(self) -> bool:
        """Check whether the stack is full.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> print(stack.full)
            False
            
        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return self._count == self.max_size

    @property
    def empty(self) -> bool:
        """Check whether the stack is empty.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> print(stack.empty)
            True
        """
        return self._count == 0

    def __eq__(self, other: object) -> bool:
        """Check if two stacks are equal.
        
        Examples:
            >>> stack1 = ArrayStack(10)
            >>> stack2 = ArrayStack(10)
            >>> print(stack1 == stack2)
            True
            
        Args:
            other (object): the object to compare to.
            
        Returns:
            bool: True if the stacks are equal, False otherwise.
        """
        if isinstance(other, ArrayStack):
            if self._count == other._count:
                if self._ar == other._ar:
                    return True
        return False

    def __ne__(self, other) -> bool:
        """Check if two stacks are not equal.
        
        Examples:
            >>> stack1 = ArrayStack(10)
            >>> stack2 = ArrayStack(10)
            >>> print(stack1 != stack2)
            False
            
        Args:
            other (object): the object to compare to.
            
        Returns:
            bool: True if the stacks are not equal, False otherwise.
        """
        return not self == other

    def __len__(self) -> int:
        """Get the number of items on the stack.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> print(len(stack))
            0
        
        Returns:
            int: the number of items on the stack.
        """
        return self._count

    def __str__(self) -> str:
        """Get a string representation of the stack.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> print(stack)
            []
        
        Returns:
            str: the string representation of the stack.
        """
        if self.empty:
            return '[]'
        else:
            string=''
            for i in range(self._count-1, -1, -1):
                string+=str(self._ar[i])+'\n'
            string=string[:-1]
            return string

    
    def __repr__(self) -> str:
        """Get a string representation of the stack.
        
        Examples:
            >>> stack = ArrayStack(10)
            >>> print(stack)
            []
        
        Returns:
            str: the string representation of the stack.
        """
        return str(self)
