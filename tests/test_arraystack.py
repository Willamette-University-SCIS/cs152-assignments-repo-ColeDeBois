# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.array_stack import ArrayStack

class TestArrayStack:
    def test_eq(self):
        sk1=ArrayStack(10) 
        sk2=ArrayStack(10)
        assert sk1==sk2
    def test_push(self):
        sk1=ArrayStack(10) 
        sk1.push('cat')
        sk1.push('car')
        assert sk1.top == 'car'
    def test_str(self):
        sk1=ArrayStack(10)
        sk1.push('cat')
        sk1.push('dog')
        string='dog\ncat'
        assert str(sk1) == string

