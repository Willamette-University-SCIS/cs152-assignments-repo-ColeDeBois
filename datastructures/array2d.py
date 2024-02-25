# datastructures.array2d.Array2D

""" This module defines an Array2D class that represents a two-dimensional array. 
    The Array class uses a datastructures.Array object as the internal data structure. 
    The Array class adheres to the docstring requirements per method, including raising 
    appropriate exceptions where indicated.
"""



from typing import Any


from datastructures.array import Array


class Array2D:
    """ Class Array2D - representing 2D data using a 1D Array
            Stipulations:
            1. Must use an Array object as the internal data 
                structure from the Array assignment.
            2. Must adhere to the docstring requirements per method, 
                including raising raising appropriate exceptions where indicated.
    """    

    def __init__(self, rows: int = 0, columns: int = 0, default_item_value = None) -> None:
        """ Array2D Constructor. Initializes the Array2D with the desired size and default value.
            
        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> print(array2d)
            [[None, None, None], [None, None, None]]

        Args:
            rows (int): the desired number of rows.
            columns (int): the desired number of columns.
            default_item_value (Any): the default value to initialize the Array2D items with.
        
        Returns:
            None
        
        Raises:
            ValueError: if the rows or columns are less than 0.
        """
        # raise NotImplementedError("Array2D.__init__")
        if rows <0 or columns <0:
            raise IndexError
        data=Array(size=rows*columns, default_item_value=default_item_value)
        
        self.data=data
        self.zero=default_item_value
        self.nrows=rows
        self.ncols=columns

    @staticmethod   
    def from_list(items: list) -> 'Array2D':
        """Create an Array2D from a 2D Python list. The function
            will take the dimensions of the list from the length of 
            of the list and the length of the first item in the list.
            The function will then create an Array2D with the same
        
        Examples:
            >>> items = [[1, 2, 3], [4, 5, 6]]
            >>> array2d = Array2D.from_list(items)
            >>> print(array2d)
            [[1, 2, 3], [4, 5, 6]]
        
        Args:
            items (list): a 2D list to create the Array2D from.
            
        Returns:    
            Array2D: the Array2D created from the 2D list.
        
        Raises:
            ValueError: if the 2D list is not rectangular or two-dimensional.
            ValueError: if list_items is not a list.
        """
        # raise NotImplementedError("Array2D.from_list")
        if not isinstance(items, list):
            raise ValueError('not a list')
        if not isinstance(items[0],list):
            raise ValueError('list is not two-dimesional')

        nrow=len(items)
        ncol=len(items[0])
        ar=Array2D(nrow,ncol)
        idx=0
        for row in items:
            if len(row) != ncol:
                raise ValueError('list is non-rectangular')
            for col in row:
                ar.data[idx]=col
                idx+=1
        return ar

    def __getitem__(self, row_index: int) -> Any:
        """ Bracket operator for accessing an item. This bracket operator is used to 
            access the first dimension (row). This should return an object that allows
            the bracket operator to be used again to access the second dimension (column).
        
        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> array2d[0][0] = 1
            >>> print(array2d[0][0])
            1
        
        Args:
            row_index (int): the index of the row to access.

        Returns:
            Any: the row object.

        Raises:
            IndexError: if the row_index is out of bounds.
        """
        # raise NotImplementedError("Array2D.__getitem__")
        if row_index < 0 or row_index >= self.nrows:
            raise IndexError

        class _row:
            def __init__(self, ncols:int, row_idx:int, data:Array):
                self.len=ncols
                self.row=row_idx
                self.data=data    
                    
            def _proj_1d(self, col_idx:int) -> int:
                '''takes a 2d index and projects it onto the corresponding index in the 1d array'''
                return self.row*self.len+col_idx
                    
            def __getitem__(self, col_idx:int) -> Any:
                if col_idx < 0 or col_idx >= self.len:
                    raise IndexError
                idx=self._proj_1d(col_idx)
                return self.data[idx]
            def __setitem__(self, col_idx:int, data:Any) -> None:
                idx=self._proj_1d(col_idx)
                self.data[idx]=data
            def __str__(self):
                string='['
                for i in range(self.len):
                    idx=self._proj_1d(i)
                    item=self.data[idx]
                    if i != self.len-1:
                        string+=str(item)+', '
                    else:
                        string+=str(item)+']'
                return string

            def __repr__(self) -> str:
                return self.__str__()

            def __eq__(self, other: object) -> bool:
                lst=[]
                for i in range(self.len):
                    i=self._proj_1d(i)
                    lst.append(self.data[i])
                return lst == other
            def __ne__(self, __o: object) -> bool:
                return not self == __o
                
        row=_row(self.ncols, row_index, self.data)
        return row
        

    @property
    def dimensions(self) -> tuple[int, int]:
        """ Property for getting dimensions of the Array2D.

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> print(array2d.dimensions)
            (2, 3)
            >>> rows, columns = array2d.dimensions
            >>> print(rows)
            2
            >>> print(columns)
            3
        
        Returns:
            tuple[int, int]: the dimensions of the Array2D.
        
        """
        # raise NotImplementedError("Array2D.dimensions")
        return (self.nrows, self.ncols)

    def resize_columns(self, new_columns: int, default_item_value: Any = None) -> None:
        """ Resize the length of the columns. Must be able to handle both increasing and 
            decreasing the size of the columns. Must not lose any data when resizing
            the columns. If the new length is smaller, then the data will be truncated.
        
        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> array2d.resize_columns(4)
            >>> print(array2d.dimensions)
            (2, 4)
            >>> array2d.resize_columns(2)
            >>> print(array2d.dimensions)
            (2, 2)

        Args:
            new_columns_len (int): the new length of the columns.
            default_item_value (Any): the default value to initialize the new items with.
        
        Returns:
            None
        
        Raises:
            ValueError: if the new_columns_len is less than 0.

        """
        # raise NotImplementedError("Array2D.resize_columns")
        if new_columns < 0:
            raise ValueError

        data_copy = self.data
        new_data = Array(new_columns*self.nrows, default_item_value)
        if new_columns != self.ncols:
            row_idx=-1
            for i in range(len(new_data)):
                i = i % new_columns
                if i == 0:
                    row_idx += 1
                if i < self.ncols:
                    new_data[i+row_idx*new_columns] = data_copy[i+row_idx*self.ncols]

            self.data=new_data
            self.ncols=new_columns
            self.zero=default_item_value
            

    def resize_rows(self, new_rows: int, default_item_value: Any = None) -> None:
        """ Resize the length of the rows. Must be able to handle both increasing and
            decreasing the size of the rows. Must not lose any data when resizing the rows.
            If the new length is smaller, then the data will be truncated.

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> array2d.resize_rows(4)
            >>> print(array2d.dimensions)
            (4, 3)
            >>> array2d.resize_rows(2)
            >>> print(array2d.dimensions)
            (2, 3)
        
        Args:
            new_rows (int): the new length of the rows.
            default_item_value (Any): the default value to initialize the new items with.

        Returns:
            None
        
        Raises:
            ValueError: if the new_rows is less than 0.
        """
        # raise NotImplementedError("Array2D.resize_rows")
        if new_rows < 0:
            raise ValueError
        new_data=Array(new_rows*self.ncols, default_item_value)
        if new_rows != self.nrows:
            for i in range(len(new_data)):
                if i < len(self.data):
                    new_data[i]=self.data[i]
                else:
                    new_data[i]=default_item_value
            self.data=new_data
            self.zero=default_item_value
            self.nrows=new_rows
 
    def __eq__(self, other: object) -> bool:
        """ Equality operator ==.

        Examples:
            >>> array2d1 = Array2D(rows=2, columns=3)
            >>> array2d2 = Array2D(rows=2, columns=3)
            >>> print(array2d1 == array2d2)
            True
            >>> array2d2[0][0] = 1
            >>> print(array2d1 == array2d2)
            False
        
        Args:
            other (object): the object to compare to.
        
        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        # raise NotImplementedError("Array2D.__eq__")
        if type(self) == type(other):
            if self.ncols == other.ncols and self.nrows == other.nrows:
                if self.data == other.data:
                    return True
        return False

    def __ne__(self, other: object) -> bool:
        """ Non-equality operator !=.
        
        Examples:
            >>> array2d1 = Array2D(rows=2, columns=3)
            >>> array2d2 = Array2D(rows=2, columns=3)
            >>> print(array2d1 != array2d2)
            False
            >>> array2d2[0][0] = 1
            >>> print(array2d1 != array2d2)
            True
        
        Args:
            other (object): the object to compare to.
        
        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        # raise NotImplementedError("Array2D.__ne__")
        return not self==other

    def __contains__(self, item: Any) -> bool:
        """ Contains operator (in).

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> print(3 in array2d)
            False
            >>> array2d[0][0] = 3
            >>> print(3 in array2d)
            True
        
        Args:
            item (Any): the item to check for.

        Returns:    
            bool: True if the item is in the Array2D, False otherwise.
        """
        # raise NotImplementedError("Array2D.__contains__")
        return item in self.data

    def clear(self) -> None:
        """ Clear operator. Clears the Array2D.

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> array2d.clear()
            >>> print(array2d)
            [[None, None, None], [None, None, None]]
        
        Returns:
            None
        """
        # raise NotImplementedError("Array2D.clear")
        self.data=Array(self.ncols*self.nrows,self.zero)

    def __str__(self) -> str:
        """ Return a string representation of the data and structure

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> print(array2d)
            [[None, None, None], [None, None, None]]
        
        Returns:
            str: the string representation of the data and structure.
        
        """
        lst=[]
        for row_idx in range(self.nrows):
            row=[]
            for col_idx in range(self.ncols):
                row.append(self.data[col_idx+row_idx*self.ncols])
            lst.append(row)
        return str(lst)

    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.

        Examples:
            >>> array2d = Array2D(rows=2, columns=3)
            >>> print(repr(array2d))
            [[None, None, None], [None, None, None]]
        
        Returns:
            str: the string representation of the data and structure.
        """
        return self.__str__()