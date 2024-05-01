from typing import Any

from datastructures.linked_list import LinkedList


class ListQueue:
    """ Class ListQueue - representing a queue based on a LinkedList
            Stipulations:
            1. Must use a LinkedList as the internal data structure from the LinkedList assignment.
            2. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
    """

    def __init__(self) -> None:
        """ Constructor.
        
        Examples:
            >>> stack = ListStack()
            
        Returns:
            None
        """
        self._lst=LinkedList()

    def enqueue(self, item: Any) -> None:
        """ Enqueue an item onto the queue.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            
        Args:
            item (Any): the item to enqueue.
        
        Returns:
            None
        """
        self._lst.append(item)

    def dequeue(self) -> Any:
        """ Dequeue an item from the queue and return the item.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> item = queue.dequeue()
            >>> print(item)
            cat
        
        Returns:
            Any: the item that is dequeued.
            
        Raises:
            IndexError: if the queue is empty.
        """
        if self.empty:
            raise IndexError
        
        item=self.front
        self._lst.pop_front()
        return item

    def clear(self) -> None:
        """ Clear the queue.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> queue.clear()
            >>> print(queue.empty)
            True
        
        Returns:
            None
        """
        self._lst.clear()

    @property
    def front(self) -> Any:
        """ Get the item at the front of the queue.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> print(queue.front)
            cat
            
        Returns:
            Any: the item that is at the front of the queue.
        
        Raises:
            IndexError: if the queue is empty.
        """
        if self.empty:
            raise IndexError
        return self._lst.front

    @property
    def empty(self) -> bool:
        """ Check if the queue is empty.
        
        Examples:
            >>> queue = ListQueue()
            >>> print(queue.empty)
            True
            
        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self._lst.empty
    def __eq__(self, other: object) -> bool:
        """ Check if the queue is equal to another queue.
        
        Examples:
            >>> queue1 = ListQueue()
            >>> queue2 = ListQueue()
            >>> print(queue1 == queue2)
            True
        
        Args:
            other (object): the object to compare to.
            
        Returns:
            bool: True if the queues are equal, False otherwise.
        """
        if isinstance(other, ListQueue):
            return self._lst == other._lst

    def __ne__(self, other: object) -> bool:
        """ Check if the queue is not equal to another queue.
        
        Examples:
            >>> queue1 = ListQueue()
            >>> queue2 = ListQueue()
            >>> print(queue1 != queue2)
            False
            
        Args:
            other (object): the object to compare to.
        
        Returns:
            bool: True if the queues are not equal, False otherwise.
        """
        return not self == other

    def __len__(self) -> int:
        """ Get the number of items in the queue.
            
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> print(len(queue))
            1
        
        Returns:
            int: the number of items in the queue.
        """
        return self._lst.__len__()

    def __str__(self) -> str:
        """ Get the string representation of the queue.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> print(queue)
            cat
        
        Returns:
            str: the string representation of the queue.
        """
        if self.empty:
            return '[]'
        else:
            string=''
            for i in self._lst:
                string+=i+'\n'
            string=string.rstrip()
            return string
    def __repr__(self) -> str:
        """ Get the string representation of the queue.
        
        Examples:
            >>> queue = ListQueue()
            >>> print(queue)
            ListQueue()
        
        Returns:
            str: the string representation of the queue.
        """
        return str(self)
    
    def __contains__(self, item: Any) -> bool:
        """ Check if the queue contains the item.
        
        Examples:
            >>> queue = ListQueue()
            >>> queue.enqueue('cat')
            >>> print('cat' in queue)
            True
        
        Args:
            item (Any): the item to check for.
        
        Returns:
            bool: True if the queue contains the item, False otherwise.
        """
        return item in self._lst
    
