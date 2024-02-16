# datastructures.array.Array
""" This module defines an Array class that represents a one-dimensional array.
The Array class is a dynamically growing array data structure.
The Array class uses a numpy array as the internal data structure.
The Array class adheres to the docstring requirements per method, including
raising appropriate exceptions where indicated.
"""
from typing import Any
import numpy as np

class Array:
    """Array class - representing a one-dimensional array.
        Stipulations:
            1. Must use a numpy array as the internal data structure.
            2. Must adhere to the docstring requirements per method, including
        raising
            raising appropriate exceptions where indicated.
    """

    def __init__(self, size: int = 0, default_item_value: Any = None) -> None:
        """ Array Constructor. Initializes the Array with a default capacity and default value.
        
        Examples:
            >>> array_one = Array()
            >>> print(array_one)
        []
        
            >>> array_two = Array(size=10)
            >>> print(array_two)
        [None, None, None, None, None, None, None, None, None, None]
        
            >>> array_three = Array(size=10, default_item_value=0)
            >>> print(array_three)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        Args:
            size (int): the desired capacity of the Array (default is 0)
            default_item_value (Any): the desired default value of the Array (default is None)
        Returns:
            None
        """
        # raise NotImplementedError('Array.__init__')
        array=[]
        for i in range(size):
            array.append(default_item_value)
        self.array=np.array(array)
        self.size=size
        self.default=default_item_value




    
    @staticmethod
    def from_list(list_items: list) -> 'Array':
        """
        Create an Array from a Python list.
        Examples:
                >>> array = Array.from_list([1, 2, 3])
                >>> print(array)
            [1, 2, 3]
            Args:
                list_items (list): the list to create the Array from.
            Returns:
            array (Array): A new Array instance containing the items from
            `list_items`
            Raises:
            TypeError: if list_items is not a list.
        """
        # raise NotImplementedError('Array.from_list')
        if not isinstance(list_items, list):
            raise TypeError
        array=Array(size=len(list_items))
        for i, item in enumerate(list_items):
            array[i]=item
            
        return array


    
    def __getitem__(self, index: int) -> Any:
        """ Bracket operator for getting an item from an Array.
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> print(array[0]) # invokes __getitem__ using the [] operator zero
        Args:
                index (int): the desired index.
        Returns:
                Any: the item at the index.
        Raises:
                IndexError: if the index is out of bounds.
        """
        # raise NotImplementedError('Array.__getitem__')
        if index >= self.size:
            raise IndexError 
        return self.array[index]
    
    def __setitem__(self, index: int, data: Any) -> None:
        """ Bracket operator for setting an item in an Array.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array[0] = 'new zero' # invokes __setitem__
            >>> print(array[0])
        new zero

        Args:
                index (int): the desired index to set.
                data (Any): the desired data to set at index.
        Returns:
                None

        Raises:
                IndexError: if the index is out of bounds.
        """
        # raise NotImplementedError('Array.__setitem__')
        if index >= self.size:
            raise IndexError
        self.array[index]=data
    
    def append(self, data: Any) -> None:
        """ Append an item to the end of the Array
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> array.append('five') # invokes append
                >>> print(array)
            [zero, one, two, three, four, five]
        Args:
                data (Any): the desired data to append.
        Returns:
                None
        """
        # raise NotImplementedError('Array.append')
        narray=np.array([self.default for i in range(self.size+1)])
        for i, item in enumerate(self.array):
            narray[i]=item
        narray[-1]=data
        self.array=narray
        self.size+=1
    
    def __len__(self) -> int:
        """ Length operator for getting the logical length of the Array (number of items in the Array).
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> print(len(array))
            5
        Returns:
                length (int): the length of the Array.
        """
        # raise NotImplementedError('Array.__len__')
        return self.size
        

    
    def resize(self, new_size: int, default_value: Any = None) -> None:
        """ Resize an Array. Resizing to a size smaller than the current size will
            truncate the Array. Resizing to a larger size will append None to the end of the
            Array.
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> array.resize(3)
                >>> print(array)
            [zero, one, two]

                >>> array.resize(5)
                >>> print(len(array))
            5

                >>> print(array)
            [zero, one, two, None, None]
        Args:
            new_size (int): the desired new size of the Array.
            default_value (Any): the desired default value to append to the Array
                if the new size is larger than the current size. Only makes sense if the new_size
                is larger than the current size. (default is None).
        Returns:
            None
        Raises:
            ValueError: if the new size is less than 0.
        """
        # raise NotImplementedError('Array.resize')
        if new_size < 0:
            raise ValueError
        narray=np.array([default_value for i in range(new_size)])
        if self.size < new_size:
            for i in range(self.size):
                narray[i]=self.array[i]
        elif new_size <= self.size:
            for i in range(new_size):
                narray[i]=self.array[i]
        self.array=narray
        self.size=new_size
        self.default=default_value

    
    def __eq__(self, other: object) -> bool:
        """ Equality operator == to check if two Arrays are equal (deep check).
        Examples:
                >>> array1 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> array2 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> print(array1 == array2)
            True
        Args:
                other (object): the instance to compare self to.
        Returns:
                is_equal (bool): true if the arrays are equal (deep check).
        """
        # raise NotImplementedError('Array.__eq__')
        if type(other) == type(Array):
            if self.size == len(other):
                for i, item in enumerate(self.size):
                    if item != other[i]:
                        return False
                return True
        else: return TypeError(f'{type(other)} cannot be compared to an Array')




    
    def __ne__(self, other: object) -> bool:
        """ Non-Equality operator !=.
        Examples:
                >>> array1 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> array2 = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> print(array1 != array2)
            False
        Args:
                other (object): the instance to compare self to.
        Returns:
                is_not_equal (bool): true if the arrays are NOT equal (deep check).
        """
        # raise NotImplementedError('Array.__ne__')
        return not self==other
    
    def __iter__(self) -> Any:
        """ Iterator operator. Allows for iteration over the Array.
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> for item in array: print(item, end=' ') # invokes iter
            zero one two three four
        Yields:
            item (Any): yields the item at index
        """
        # raise NotImplementedError('Array.__iter__')
        for i in range(self.size):
            yield self.array[i]
        
    
    def __reversed__(self) -> Any:
        """ Reversed iterator operator. Allows for iteration over the Array in
        reverse.
        Examples:
                >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
                >>> for item in reversed(array): print(item, end= ' ') # invokes __reversed__
            four three two one zero
        Yields:
                item (Any): yields the item at index starting at the end
        """
        # raise NotImplementedError('Array.__reversed__')
        for i in range(self.size-1,-1,-1):
            yield self.array[i]

    def __delitem__(self, index: int) -> None:
        """ Delete an item in the array. Copies the array contents from index + 1
            down to fill the gap caused by deleting the item and shrinks the array size
            down by one.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> del array[2]
            >>> print(array)
        [zero, one, three, four]

            >>> len(array)
            4

        Args:
            index (int): the desired index to delete.
        Returns:
            None
        """
        # raise NotImplementedError('Array.__delitem__')
        narray=np.array([self.default for i in range(self.size-1)])
        for i, item in enumerate:
            if i != index:
                narray[i]=item
        self.array=narray
        self.size-=1
        
    
    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in). Checks if the array contains the item.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print('three' in array)
        True

        Args:
            item (Any): the desired item to check whether it's in the array.
        Returns:
            contains_item (bool): true if the array contains the item.
        """
        raise NotImplementedError('Array.__contains__')
    
    def __does_not_contain__(self, item: Any) -> bool:
        """ Does not contain operator (not in)
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print('five' not in array)
        True

        Args:
            item (Any): the desired item to check whether it's in the array.
        Returns:
            does_not_contains_item (bool): true if the array does not contain the
        item.
        """
        raise NotImplementedError('Array.__does_not_contain__')
    
    def clear(self) -> None:
        """ Clear the Array
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> array.clear()
            >>> print(array)
        []

            >>> print(len(array))
        0
        Returns:
            None
        """
        # raise NotImplementedError('Array.clear')
        self.array=Array(default_item_value=self.default)
        self.size=0
    
    def __str__(self) -> str:
        """ Return a string representation of the data and structure.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(array)
        [zero, one, two, three, four]

        Returns:
            string (str): the string representation of the data and structure.
        """
        # raise NotImplementedError('Array.__str__')
        return str(self.array)
    
    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.
        Examples:
            >>> array = Array.from_list(['zero', 'one', 'two', 'three', 'four'])
            >>> print(repr(array))
        [zero, one, two, three, four]

        Returns:
            string (str): the string representation of the data and structure.
        """
        return self.array.__str__()


