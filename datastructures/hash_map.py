from __future__ import annotations

from collections.abc import Iterable
import copy
from typing import Any, NamedTuple
from sympy import nextprime

from datastructures.array import Array
from datastructures.linked_list import LinkedList

class Pair(NamedTuple):
    """ Pair class - representing a key-value pair in the HashMap.
    
        Attributes:
            key (Any): The key of the pair.
            value (Any): The value of the pair.
    """
    key: Any
    value: Any

class HashMap:
    """ Class HashMap - representing a HashMap (dictionary) where the
        buckets are based on an Array and the chains are based on LinkedLists
            Stipulations:
            1. Must use an Array<LinkedList<Pair>> as the internal data structure from the
                Array, LinkedList and Tuple assignments.
            2. Must adhere to the docstring requirements per method, including raising
                raising appropriate exceptions where indicated.
            3. If the percentage of filled buckets passes a given or default threshold, resize the hash map
                to the next highest prime 
    """

    default_load_factor_threshold = 0.6

    def default_hash_function(key: Any, capacity: int) -> int:
        """ Default hash function for the HashMap class, supports scalar and iterable keys.
            
            Args:
                key (Any): The key to hash.
                capacity (int): The capacity of the hash map.
                
            Returns:
                int: The hash of the key for a container containing the given capacity.
        """
        if isinstance(key, Iterable):
            return sum([hash(val) for val in key]) % capacity
        
        return hash(key) % capacity

    def __init__(self, capacity: int = 7, hash_function=default_hash_function, load_factor_threshold: float = default_load_factor_threshold) -> None:
        """ Constructor for the HashMap class.
            
            Examples: 
                >>> hashmap = HashMap(23)
                >>> hashmap['x'] = 3
                >>> hashmap['x']
                3
            
            Args:
                capacity (int): The capacity of the hashmap (number of buckets).
                hash_function (function): The hash function to override the default class 
                    hash function.
                
            Raises:
                TypeError: If the hash function is not a function.
                ValueError: If the capacity is less than 0.
                ValueError: If the load factor threshold is less than 0 or greater than 1.
        """
        self._buckets = Array(capacity)
        for i in range(capacity):
            self._buckets[i]=LinkedList()
        self._hash = hash_function 
        self._load_factor_threshold=load_factor_threshold
        self._count=0
        


    
    def _new_bucket_capacity(self) -> int:
        """ Private method to determine the best new bucket size based on the current count and the load factor threshold.
            Returns:
                int: The best bucket size.
        """
        return nextprime(int(self._count / self._load_factor_threshold)) 

    @staticmethod
    def from_dictionary(py_dict: dict) -> HashMap:
        """ Create a new HashMap from a Python dictionary. Base the size of the HashMap on the number of keys in the dictionary
            such that the load factor is less than 60%.

        Examples:
            >>> hashmap = HashMap.from_dictionary({'x': 3, 'y': 4})
            >>> hashmap['x']
            3
            >>> hashmap['y']
            4
        
        Args:
            py_dict (dict): The dictionary to convert.
        
        Returns:
            HashMap: The new HashMap.

        Raises:
            TypeError: If the input is not a dictionary.
        """
        if not isinstance(py_dict, dict):
            raise TypeError
        hmap = HashMap(int(len(py_dict)/0.6))
        for key, value in py_dict.items():
            hmap[key] = value
        return hmap

    def __getitem__(self, key: Any) -> Any:
        """ Bracket operator for getting a value from the hash map. If the key is not present, raise a KeyError.

            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap['x'] = 3
                >>> hashmap['x']
                3

            Args:
                key (Any): The key to get the value of.

            Returns:
                Any: The value of the key.

            Raises:
                KeyError: If the key is not present in the hashmap.
        """
        if not key in self.keys():
            raise KeyError
        key_hash=self._hash(key,self.capacity)
        for item in self._buckets[key_hash]:
            if item[0]==key:
                return item[1]


    def __setitem__(self, key: Any, value: Any) -> None:
        """ Bracket operator for setting a value in the hash map. If the key is already present, replace the value.
            If the load factor is greater than the threshold, resize the hash map.
            
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap['x'] = 3
                >>> hashmap['x']
                3
                
            Args:
                key (Any): The key to set the value of. 
                value (Any): The value to set.

            Returns:
                None
            """
        pair=Pair(key,value)
        if not pair in self.items():
            key_hash=self._hash(key,self.capacity)
            if not key in self.keys():
                self._buckets[key_hash].append(pair)
            else:
                del self[key]
                self._buckets[key_hash].append(pair)
            self._count+=1
        if self._count/self.capacity >= self._load_factor_threshold:
                newsize=self._new_bucket_capacity()
                self.resize_and_rehash(newsize, self._hash)
        
            

    @property
    def capacity(self) -> int:
        """ Get the capacity of the hash map (number of buckets)
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap.capacity
                23
            
            Returns:
                int: The capacity of the hash map.
        """
        return len(self._buckets)

    def __len__(self) -> int:
        """ Length operator for the hash map. Returns the count of the hash map.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> len(hashmap)
                0
                
            Returns:
                int: The count of the hash map.
        """
        if self._count < 0:
            return 0
        else: return self._count

    def resize_and_rehash(self, new_table_size: int, new_hash_function) -> None:
        """ Resize the hash map to a new table size and rehash the items.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap.resize_and_rehash(7, lambda key: key % 7)
                
            Args:
                new_table_size (int): The new table size.
                new_hash_function (function): The new hash function to use.
            
            Returns:
                None
            """
        new_buckets=Array(new_table_size, default_item_value=LinkedList())
        # for idx in new_buckets:
        #     idx=LinkedList()
        for bucket in self._buckets:
            for pair in bucket:
                key_hash=self._hash(pair[0],new_table_size)
                new_buckets[key_hash].append(pair)

    
    def __del__(self, key: Any) -> None:
        """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> del hashmap['x']
            
            Args:
                key (Any): The key to delete.
                
            Returns:
                None
        """
        if  key not in self.keys():
            raise KeyError
    
        key_hash=self._hash(key,self.capacity)
        llist=self._buckets[key_hash]
        for i in llist:
            if i[0]==key:
                llist.extract(i)
        self._count-=1
        
    def __eq__(self, other: 'HashMap') -> bool:
        """ Equality operator for the hash map. Returns true if the hash maps are equal.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap2 = HashMap(23)
                >>> hashmap == hashmap2
                True
            
            Args:
                other (HashMap): The other hash map to compare to.
                
            Returns:
                bool: True if the hash maps are equal.
            """
        if isinstance(other,HashMap):
            if self.capacity==other.capacity and self._count==other._count:
                for i in range(len(self)):
                    if self._buckets[i]!=other._buckets[i]:
                        return False
                return True
        return False
                
    
    def __ne__(self, other: 'HashMap') -> bool:
        """ Inequality operator for the hash map. Returns true if the hash maps are not equal.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap2 = HashMap(23)
                >>> hashmap != hashmap2
                False
            
            Args:
                other (HashMap): The other hash map to compare to.
                
            Returns:
                bool: True if the hash maps are not equal.
            """
        
        return not self==other

    def __iter__(self) -> Any:
        """ Iterator for the hash map. Returns an iterator of the keys.

            Examples:
                >>> hashmap = HashMap(23)
                >>> for key in hashmap:
                ...     print(key)

            Returns:    
                Any: An iterator of the keys.
        """
        for llist in self._buckets:
            for item in llist:
                yield item[0]

    def __delitem__(self, key: Any) -> None:
        """ Delete an item in the hash map. Does not resize the buckets, but does remove the associated chain link.
        Examples:
            >>> hashmap = HashMap(23)
            >>> del hashmap['x']

            Args:
                key (Any): The key to delete.
                
            Returns:
                None
        """
        self.__del__(key)

    @property
    def load_factor(self) -> float:
        """ Get the current load factor of the hash map (count / capacity).
        
            Examples:
                >>> hashmap = HashMap(23, default_load_factor_threshold=0.6)
                >>> hashmap.current_load_factor
                0.0
            
            Returns:
                float: The current load factor of the hash map.
        """
        return self._count/self.capacity
    
    @property
    def load_factor_threshold(self) -> float:
        """ Get the load factor threshold of the hash map.
        
            Examples:
                >>> hashmap = HashMap(23, default_load_factor_threshold=0.6)
                >>> hashmap.load_factor_threshold
                0.6
            
            Returns:
                float: The load factor threshold of the hash map.
        """
        return self._load_factor_threshold


    def __contains__(self, key: Any) -> bool:
        """ Contains operator for the hash map. Returns true if the key is in the hash map. 
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> 'x' in hashmap
                False
                
            Args:
                key (Any): The key to check for.
            
            Returns:
                bool: True if the key is in the hash map.
        """
        for i in self.keys():
            if i==key:
                return True
        return False

    def clear(self) -> None:
        """ Clear the hash map. Removes all items from the hash map.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap.clear()
                
            Returns:
                None
        """
        self._buckets=Array(self.capacity, default_item_value=LinkedList)

    def keys(self) -> list:
        """ Returns a view object. The view object contains the keys of the dictionary, as a list.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> keys = hashmap.keys()
                >>> for key in keys:
                ...     print(key)
                0
                1
                2
                3
                4
                5
                6
                
            Returns:
                list: The keys of the hash map.
        """
        list=[]
        for llist in self._buckets:
            for item in llist:
                list.append(item[0])
        return list


    def values(self) -> list:
        """ Returns a view object. The view object contains the values of the dictionary, as a list.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> values = hashmap.values()
                >>> for value in values:
                ...     print(value)
                0
                1
                2
                3
                4
                5
                6
            
            Returns:
                list: The values of the hash map.
        """
        list=[]
        for llist in self._buckets:
            for item in llist:
                list.append(copy.deepcopy(item[1]))
        return list

    def items(self) -> list:
        """ Returns a view object. The view object contains the key-value pairs of the dictionary, as a list of tuples.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> hashmap['x'] = 3
                >>> items = hashmap.items()
                >>> for key, value in items:
                ...     print(key, value)
                x 3
            
            Returns:
                list: The items of the hash map.
        """
        list=[]
        for llist in self._buckets:
            for item in llist:
                list.append(copy.deepcopy(item))
        return list

    def __str__(self) -> str:
        """ String representation of the hash map.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> print(hashmap)
                HashMap count: 0, Items: Array(
        """
        string="HashMap count: "+str(self._count)+", Items: "
        for item in self.items():
            string+=str(item)+",\n "
        return string
    
    def __repr__(self) -> str:
        """ Representation of the hash map.
        
            Examples:
                >>> hashmap = HashMap(23)
                >>> print(hashmap)
                HashMap count: 0, Items: Array(
        """
        return self.__str__()