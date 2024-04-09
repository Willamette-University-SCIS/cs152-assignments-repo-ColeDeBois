# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.hash_map import HashMap

class TestHashMap:
    def test_from_dict(self):
        hmap=HashMap().from_dictionary({'a':1,'b':2,'c':3})
        hmap
