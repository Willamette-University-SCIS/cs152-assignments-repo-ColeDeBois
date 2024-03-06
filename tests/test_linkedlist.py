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
        llist=LinkedList.from_list(['apple', 'banana', 'jalapeno'])
        llist.prepend('test')

        assert llist.front == 'test'

    def test_insert_after(self):
        llist=LinkedList.from_list(['apple', 'jalapeno'])
        llist.insert_after('apple','banana')
        assert llist == LinkedList.from_list(['apple', 'banana', 'jalapeno'])
        

    def test_insert_before(self):
        llist=LinkedList.from_list(['a','b','d'])
        llist.insert_before('d','c')
        assert llist == LinkedList.from_list(['a', 'b', 'c', 'd'])
        assert llist.back == 'd'

    
    def test_key_error(self):
        llist=LinkedList()
        try:
            llist.insert_before('e','e')
        except KeyError:
            try:
                llist.insert_after('e','e')
            except KeyError:
                pass



    

        



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


    def test_contains_(self):
        lista=['apple', 'banana', 'jalapeno']
        llist=LinkedList.from_list(lista)
        assert 'apple' in llist




        
