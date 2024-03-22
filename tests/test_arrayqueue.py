# This is a file you can copy/paste to create a new test file.
# Just make sure the new name starts with test_ and ends with .py.

# import data structures like this:
# from datastructures.array import Array
from datastructures.array_queue import ArrayQueue


class TestArrayQueue:
    def test_front(self):
        que=ArrayQueue(10)
        que.enqueue('cat')
        assert que.front == 'cat'
    
    def test_dequeue(self):
        que=ArrayQueue(10)
        que.enqueue('cat')
        que.enqueue('dog')
        assert que.dequeue() == 'cat'
    
    def test_str(self):
        que=ArrayQueue(10)
        que.enqueue('cat')
        assert str(que) == 'cat'

    def test_wrapping(self):
        que=ArrayQueue(5)
        lst=['cat','dog','rock','bird','snake','totoro']

        que.enqueue(lst[0])
        que.enqueue(lst[1])
        que.enqueue(lst[2])
        que.enqueue(lst[3])
        assert que.dequeue() == lst[0]
        que.enqueue(lst[4])
        que.enqueue(lst[5])
        assert que.dequeue() == lst[1]
        assert que.dequeue() == lst[2]
        assert que.dequeue() == lst[3]
        assert que.dequeue() == lst[4]
        assert que.dequeue() == lst[5]
        assert que.empty == True
