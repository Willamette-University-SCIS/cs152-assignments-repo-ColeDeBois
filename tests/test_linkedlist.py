# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.linked_list import LinkedList


class TestLinkedList:
    def test_iter(self):
        lista=['apple', 'banana', 'jalapeno']
        llist=LinkedList.from_list(lista)
        listb=[]
        for item in llist:
            listb.append(item)
        assert listb == lista

    def test_reversed(self):
        lista=['apple', 'banana', 'jalapeno']
        llist=LinkedList.from_list(lista)
        listb=[]
        for item in reversed(llist):
            listb.append(item)
        lista.reverse() 
        assert listb == lista

    def test_eq(self):
        list=['apple', 'banana', 'jalapeno']
        llista=LinkedList.from_list(list)
        llistb=LinkedList.from_list(list)

        assert llista==llistb

    def test_prepend(self):
        raise NotImplemented
        



    def test_indexerrors(self):
        #mega indexerror tester 
        llist=LinkedList()
        try:
            llist.back
        except IndexError:
            pass
        try:
            llist.front
        except IndexError:
            pass
        try:
            llist.pop_back
        except IndexError:
            pass
        try:
            llist.pop_front
        except IndexError:
            pass

    def test_keyerrors(self):
        llist=LinkedList.from_list(['a','b','c'])
        with None as KeyError:
            llist.extract('d')
            llist.insert_after('d',None)
            llist.insert_before('d',None)
            



        


    def test_contains_(self):
        lista=['apple', 'banana', 'jalapeno']
        llist=LinkedList.from_list(lista)
        assert 'apple' in llist




        
