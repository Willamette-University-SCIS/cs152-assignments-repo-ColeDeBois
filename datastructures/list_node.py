from __future__ import annotations
from typing import Any

class ListNode:
    """ ListNode - represents a node in a linked list
            Stipulations:
            1. Must adhere to the docstring requirements per method, including raising
               raising appropriate exceptions where indicated.
    """

    def __init__(self, item: Any, previous_node: ListNode | None = None, next_node: ListNode | None = None) -> None:
        """ Constructor - represents a node in a linked list.

            Examples:
                >>>node = ListNode('cat')  # Create a new node with 5 and no previous or next node.
                >>>node = ListNode('cat', None, None)  # Create a new node with 'cat' and no previous or next node.
                >>>print(node)
                cat

            Args:
                item (Any): the item (data) to store in the node
                previous_node (ListNode | None): the corresponding previous node of this node in the linked list
                next_node (ListNode | None): the corresponding next node of this node in the linked list
        """
        # raise NotImplementedError("ListNode.__init__")
        self._data=item
        self._previous_node=previous_node
        self._next_node=next_node

    @property
    def item(self) -> Any:
        """ Property getter for the item.
            
        Examples:
            >>>node = ListNode('cat')
            >>>item = node.item
            >>>print(item)
            cat
        
        Returns:
            Any: the item stored in the node.
        """
        # raise NotImplementedError("ListNode.item")
        return self._data

    @item.setter
    def item(self, item: Any) -> None:
        """ Property setter for the item.
        
        Examples:
            >>>node = ListNode('cat')
            >>>node.item = 'dog'
            >>>print(node)
            dog
        
        Args:
            item (Any): the item to store in the node.
            
        Returns:
            None
        """
        # raise NotImplementedError("ListNode.item")
        self._data=item

    @property
    def previous(self) -> ListNode | None:
        """ Property getter for the previous node.

        Examples:
            >>>node1 = ListNode('cat')
            >>>node2 = ListNode('dog', previous_node=node1)
            >>>print(node2.previous)
            cat
        
        Returns:
            ListNode | None: the previous node of the node.
        """      
        # raise NotImplementedError("ListNode.previous")
        return self._previous_node

    @previous.setter
    def previous(self, previous_node: ListNode) -> None:
        """ Property setter for the previous node.

        Examples:
            >>>node1 = ListNode('cat')
            >>>node2 = ListNode('dog')
            >>>node2.previous = node1
            >>>print(node2.previous)
            cat

        Args:
            previous_node (ListNode): the node's previous_node instance.
        """
        # raise NotImplementedError("ListNode.previous")
        self._previous_node = previous_node

    @property
    def next(self) -> ListNode | None:
        """ Property getter for the next node.
        
        Examples:
            >>>node1 = ListNode('cat')
            >>>node2 = ListNode('dog', next_node=node1)
            >>>print(node2.next)
            cat
        
        Returns:
            ListNode | None: the next node of the node.
        """
        # raise NotImplementedError("ListNode.next")
        return self._next_node

    @next.setter
    def next(self, next_node: ListNode) -> None:
        """ Property setter for the next node.
        
        Examples:
            >>>node1 = ListNode('cat')
            >>>node2 = ListNode('dog')
            >>>node2.next = node1
            >>>print(node2.next)
            cat
        
        Args:
            next_node (ListNode): the node's next_node instance.
        
        Returns:
            None
        """
        # raise NotImplementedError("ListNode.next")
        self._next_node=next_node

    def __eq__(self, other: object) -> bool:
        """ Equality operator ==.

            Examples:
                >>>node1 = ListNode('cat')
                >>>node2 = ListNode('cat')
                >>>node3 = ListNode('dog')
                >>>print(node1 == node2)
                True
                >>>print(node1 == node3)
                False

            Args:
                other (object): the instance to compare self to.
            
            Returns:
                bool: true if the nodes are equal (deep check). false if other is not a ListNode or they are not equal.
        """
        # raise NotImplementedError("ListNode.__eq__")
        return self.item == other.item

    def __str__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>>node = ListNode('cat')
            >>>print(node)
            cat
        
        Returns:
            str: the string representation of the data and structure.
        """
        # raise NotImplementedError("ListNode.__str__")
        return str(self._data)

    def __repr__(self) -> str:
        """ Return a string representation of the data and structure.
        
        Examples:
            >>>node = ListNode('cat')
            >>>print(node)
            cat
        
        Returns:
            str: the string representation of the data and structure.
        """
        # raise NotImplementedError("ListNode.__repr__")
        return self.__str__()
