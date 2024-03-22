# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.list_stack import ListStack

class TestListStack:
    def test_eq(self):
        sk1=ListStack()
        sk1.push('car') 
        sk2=ListStack()
        sk2.push('car') 
        assert sk1==sk2
    def test_push(self):
        sk1=ListStack() 
        sk1.push('cat')
        sk1.push('car')
        assert sk1.top == 'car'
    def test_str(self):
        sk1=ListStack()
        sk1.push('cat')
        sk1.push('dog')
        sk1.pop()
        sk1.pop()
        assert str(sk1) == '[]'

    def test_len(self):
        sk=ListStack()
        for i in range(10):
            sk.push('a')
        sk.pop()
        assert len(sk) == 9
