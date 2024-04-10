# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.hash_map import HashMap
from .car import Car

class TestHashMap:
    def test_from_dict(self):
        hmap=HashMap.from_dictionary({'a':1,'b':2,'c':3})
        assert hmap['a'] == 1
    def test_init(self):
        hmap=HashMap()
        hmap['a']=1
        assert hmap['a'] == 1
    
    def test_del(self):
        hmap=HashMap()
        hmap['a']=1
        del hmap['a']
        assert not 'a' in hmap
    
    def test_set_repeat(self):
        hmap=HashMap()
        hmap['a']=1
        hmap['b']=2
        hmap['a']=1
        assert len(hmap) == 2

    def test_reset(self):
        hmap=HashMap()
        hmap['a']=1
        hmap['a']=2
        assert hmap['a'] == 2
    
    
