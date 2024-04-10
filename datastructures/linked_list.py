from __future__ import annotations
from typing import Any

from datastructures.list_node import ListNode
from datastructures.array import Array

class LinkedList:
    """ Class LinkedList - representing an unordered linked list
        Depends on ListNode class to store the data, previous, and next nodes.
            Stipulations:
            1. Must manage the linked list using two ListNode objects (_head and _tail)
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
    """

    def __init__(self) -> None:
        """ Constructor for the LinkedList constructs an empty linked list.

        Examples:
            >>> linked_list = LinkedList()
            >>> print(linked_list)
            []
        
        Returns:
            None
        
        """
        # raise NotImplementedError('LinkedList.__init__')
        self._head=None
        self._tail=None
        self._count=0
        

    @staticmethod
    def from_list(py_list: list) -> LinkedList:
        """ Create a new LinkedList from a Python list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
        
        Args:
            py_list (list): list to convert to a linked list.

        Returns:
            A new LinkedList instance.
        
        Raises:
            TypeError: if py_list is not a list.
        """
        # raise NotImplementedError('LinkedList.from_list')
        if not isinstance(py_list, list):
            raise TypeError
        llist=LinkedList()
        for item in py_list:
            llist.append(item)
        return llist
                
    
    def append(self, item: Any) -> None:
        """ Append an item to the end of the list.

        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.append('cat')
            >>> linked_list.append('dog')
            >>> print(linked_list)
            ['cat', 'dog']
        
        Args:
            item: the desired data to append to the linked list.
        
        Returns:
            None
        """
        # raise NotImplementedError('LinkedList.append')
        node=ListNode(item, previous_node=self._tail, next_node=None)
        if self._count == 0:
            self._head=self._tail=node
        else:
            self._tail.next=node
            self._tail=node
        self._count+=1

    def prepend(self, item: Any) -> None:
        """ Prepend an item to the beginning of the list.
        
        Examples:
            >>> linked_list = LinkedList()
            >>> linked_list.prepend('cat')
            >>> linked_list.prepend('dog')
            >>> print(linked_list)
            ['dog', 'cat']
        
        Args:
            item (Any): the desired data to prepend to the linked list.
            
        Returns:
            None
        
        """
        # raise NotImplementedError('LinkedList.prepend')
        node=ListNode(item, previous_node=None, next_node=self._head)
        if self._count == 0:
            self._head=self._tail=node
        else:
            self._head.previous=node
            self._head=node
        self._count+=1

    def insert_before(self, before_item: Any, new_item: Any) -> None:
        """ Insert a new item before a specified item.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.insert_before('dog', 'fish')
            >>> print(linked_list)
            ['cat', 'fish', 'dog', 'bird']
                
        Args:
            before_item (Any): the item that the user wishes to insert before.
            new_item (Any): the desired item to insert.
        
        Returns:
            None
        
        Raises:
            KeyError: if before_item is not found.
        """
        # raise NotImplementedError('LinkedList.insert_before')
        if self._count < 1:
            raise KeyError
        done =False
        travel=self._head
        if self.front == before_item:
            self.prepend(new_item)
        else:
            while not done:
                if travel.item == before_item:
                    prev_node=travel.previous
                    new_node=ListNode(new_item,prev_node,travel)
                    prev_node.next=new_node
                    travel.previous=new_node
                    self._count+=1
                    done=True
                elif travel.next == None:
                    raise KeyError
                travel=travel.next
            


    def insert_after(self, after_item: Any, new_item: Any) -> None:
        """ Insert a new item after a specified item.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.insert_after('dog', 'fish')
            >>> print(linked_list)
            ['cat', 'dog', 'fish', 'bird']

        Args:
            after_item (Any): the item that the user wishes to insert after.
            new_item (Any): the desired item to insert.

        Returns:
            None

        Raises:
            KeyError: if after_item is not found.
        
        """
        # raise NotImplementedError('LinkedList.insert_after')
        if self._count < 1:
            raise KeyError
        done =False
        travel=self._head
        if self.back == after_item:
            self.append(new_item)
        else:
            while not done:
                if travel.item == after_item:
                    next_node=travel.next
                    new_node=ListNode(new_item,travel,next_node)
                    next_node.previous=new_node
                    travel.next=new_node
                    self._count+=1
                    done=True
                elif travel.next == None:
                    raise KeyError
                travel=travel.next

    @property
    def head(self) -> ListNode | None:
        """ Return the ListNode instance pointing at the head of the linked list.
            Note: this method should be used for debug and test purposes only.
            
        Examples
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> head = linked_list.head
            >>> print(head.item)
            cat
        
        Returns:
            head (ListNode | None): the ListNode instance representing the head of the linked list.
            
        """
        # raise NotImplementedError('LinkedList.head')
        return self._head

    @property
    def tail(self) -> ListNode | None:
        """ Return the ListNode instance pointing at the tail of the linked list.
            Note: this method should be used for debug and test purposes only.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> tail = linked_list.tail
            >>> print(tail.item)
            bird
        
        Returns:
            tail (ListNode | None): the ListNode instance representing the tail of the linked list.
        """
        # raise NotImplementedError('LinkedList.tail')
        return self._tail

    @property
    def front(self) -> Any:
        """ Return the item at the front of the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> first_item = linked_list.front
            >>> print(first_item)
            cat
        
        Returns:
            front (Any): the item stored in the head of the list
            
        Raises:
            IndexError: if the list is empty.
        
        """
        # raise NotImplementedError('LinkedList.front')
        if self._count == 0:
            raise IndexError
        return self.head.item

    @property
    def back(self) -> Any:
        """ Return the item at the back of the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> last_item = linked_list.back
            >>> print(last_item)    
            bird

        Returns:
            last (Any): the item stored in the tail of the list.
        
        Raises:
            IndexError: if the list is empty.
        """
        # raise NotImplementedError('LinkedList.back')
        if self._count == 0:
            raise IndexError
        return self.tail.item

    def clear(self) -> None:
        """ Clear the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.clear()
            >>> print(linked_list)
            []
        
        Returns:
            None
        """
        # raise NotImplementedError('LinkedList.clear')
        self._head=None
        self._tail=None
        self._count=0

    def extract(self, item: Any) -> None:
        """ Extract an item from the Linked List.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.extract('dog')
            >>> print(linked_list)
            ['cat', 'bird']

        Args:
            item (Any): the item to remove from the linked list.

        Returns:
            None

        Raises:
            KeyError: if the item is not found.
        """
        # raise NotImplementedError('LinkedList.extract')
        if not item in self:
            raise KeyError
        travel=self.head.next
        
        if self.front == item:
            self.pop_front()
        elif self.back == item:
            self.pop_back()
        else:
            while travel is not self.back:
                if travel.item == item:
                    next_node=travel.next
                    prev_node=travel.previous
                    next_node.previous=prev_node
                    prev_node.next=next_node
                    break
                travel=travel.next
            self._count-=1

    @property
    def empty(self) -> bool:
        """ Property to determine whether the list is empty.
        
        Examples:
            >>> linked_list = LinkedList()
            >>> print(linked_list.empty)
            True
        
        Returns:
            bool: whether the list is empty.
        """
        # raise NotImplementedError('LinkedList.empty')
        return self._count == 0

    def pop_front(self) -> None:
        """ Remove the first item in the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.pop_front()
            >>> print(linked_list)
            ['dog', 'bird']
        
        Returns:
            None
        
        Raises:
            IndexError: if the list is empty.
            
        """
        # raise NotImplementedError('LinkedList.pop_front')
        if self._count == 0:
            raise IndexError
        new_head=self._head.next
        self._head=new_head
        self._count-=1

    def pop_back(self) -> None:
        """ Remove the last item in the linked list.

        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list.pop_back()
            >>> print(linked_list)
            ['cat', 'dog']

        Returns:
            None
        
        Raises:
            IndexError: if the list is empty.
        """
        # raise NotImplementedError('LinkedList.pop_back')
        if self._count == 0:
            raise IndexError
        new_tail=self._tail.previous
        self._tail=new_tail
        self._count-=1

    def __contains__(self, item: Any) -> bool:
        """ Membership operator in.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print('dog' in linked_list)
            True
        
        Args:
            item (Any): the item to search for.
            
        Returns:
            bool: whether the linked list contains the item.
        """
        # raise NotImplementedError('LinkedList.__contains__')
        for i in self:
            if i==item:
                return True
        return False

    def __eq__(self, other: object) -> bool:
        """ Equality operator ==.
        
        Examples:
            >>> linked_list1 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list2 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list1 == linked_list2)
            True
        
        Args:
            other (object): the instance to compare self to.
            
        Returns:
            bool: whether the lists are equal (deep check).
        """
        # raise NotImplementedError('LinkedList.__eq__')
        if self._count == other._count:
            onode = other._head
            for i in self:
                if i != onode.item:
                    return False
                onode = onode.next
            return True
        return False

    def __ne__(self, other: object) -> bool:
        """ Non-Equality operator !=.
        
        Examples:
            >>> linked_list1 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> linked_list2 = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list1 != linked_list2)
            False
        
        Args:
            other (object): the instance to compare self to.
            
        Returns:
            bool: whether the lists are not equal (deep check).
        """
        # raise NotImplementedError('LinkedList.__ne__')
        return not self == other
    
    def __iter__(self) -> Any:
        """ Iterator operator.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> for item in linked_list:
            ...     print(item)
            cat
            dog
            bird
        
        Returns:
            Any: yields the item at ListNode.
        """
        # raise NotImplementedError('LinkedList.__iter__')
        node=self._head
        for i in range(self._count):
            yield node.item
            node=node.next

    def __reversed__(self) -> Any:
        """ Reversed iterator operator.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> for item in reversed(linked_list):
            ...     print(item)
            bird
            dog
            cat
        
        Returns:
            Any: yields the item at ListNode.
        """
        # raise NotImplementedError('LinkedList.__reversed__')
        node=self._tail
        for i in range(self._count):
            yield node.item
            node=node.previous

    def __len__(self) -> int:
        """ len operator for getting length of the linked list.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> size = len(linked_list)
            >>> print(size)
            3
        
        Returns:
            int: the length of the LinkedList.
        """
        # raise NotImplementedError('LinkedList.__len__')
        return self._count

    def __str__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
            
        Returns:
            str: the string representation of the data and structure.
            
        """
        # raise NotImplementedError('LinkedList.__str__')
        lst=[]
        for node in self:
            lst.append(str(node))
        return str(lst)

    
    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>> linked_list = LinkedList.from_list(['cat', 'dog', 'bird'])
            >>> print(linked_list)
            ['cat', 'dog', 'bird']
            
        Returns:
            str: the string representation of the data and structure.
        
        """
        # raise NotImplementedError('LinkedList.__repr__')
        return self.__str__()
    
    def to_array(self):
        """ Convert the contents of the LinkedList to an Array.
        Example:
            »> print(my_linked_list)
            15, 7, 17, 13, 111
            >> my_array = my_linked _list. to_array ()
            >> print(my_array)
            15, 7, 17, 13, 111

        Args:
            none
        Returns:
            Array: an array containing the items from the Linked List """
        array=Array()
        for i in self:
            array.append(i)
        return array