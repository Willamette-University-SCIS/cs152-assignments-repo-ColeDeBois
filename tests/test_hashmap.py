# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.hash_map import HashMap
from .car import Car, Color, Make, Model
car1=Car(vin='123', color=Color.RED, make=Make.TOYOTA, model=Model.CAMRY)
car2=Car(vin='456', color=Color.RED, make=Make.FORD, model=Model.FOCUS)
car3=Car(vin='789', color=Color.RED, make=Make.HONDA, model=Model.CIVIC)

class TestHashMap:
    def test_complex_set(self):
        hmap=HashMap()
        hmap[car1]=1
        hmap[car1]=3
        assert hmap[car1] == 3

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
        for i in range(10):
            hmap[str(i)]=i
        hmap['5']=7
        assert len(hmap) == 10
        assert len(hmap.items()) == 10
    
    def test_set_capacity(self):
        hmap=HashMap()
        for i in range(100):
            hmap[str(i)]=i
        assert len(hmap) == 100
    def test_capacity(self):
        hmap=HashMap(23)
        assert hmap.capacity == 23
        assert len(hmap) == 0
        
    
    
