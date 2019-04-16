from set import Set
from set import CircularBuffer
import unittest


class SetTest(unittest.TestCase):

    def test_contains(self):
        new_set = Set(['l',1,2,3,'r','t','y','u','s','q'])
        assert new_set.contains('l') == True
        assert new_set.contains('q') == True
        assert new_set.contains(3) == True
        assert new_set.contains('t') == True
        assert new_set.contains('e') == False
        assert new_set.size == 10

    def test_add(self):
        new_set = Set(['l'])
        new_set.add('3')
        new_set.add(None)
        new_set.add('5')
        new_set.add('l')
        new_set.add(3)
        assert new_set.contains('l') == True
        assert new_set.contains(3) == True
        assert new_set.contains('5') == True
        assert new_set.contains(None) == True
        assert new_set.size == 5


    def test_remove(self):
        new_set = Set(['l',1,2,3,'r','t','y','u','s','q'])
        assert new_set.size == 10
        new_set.remove("l")
        new_set.remove("r")
        new_set.remove("q")
        new_set.remove("u")
        assert new_set.contains('l') == False
        assert new_set.contains("r") == False
        assert new_set.contains('q') == False
        assert new_set.contains("u") == False
        assert new_set.size == 6

    def test_union(self):
        new_set = Set(['l',1,2,3,'r','t','y','u','s','q'])
        other_set  = Set(['p',8,9,4])

        union_set = new_set.union(other_set)

        assert union_set.contains('p') == True
        assert union_set.contains('r') == True
        assert union_set.contains(1) == True
        assert union_set.contains("{") == False

    def test_intersection(self):
        new_set = Set(['l',1,2,3,'r','t','y','u','s','p'])
        other_set  = Set(['p',2,3,4])

        intersection_set = new_set.intersection(other_set)


        assert intersection_set.contains(2) == True
        assert intersection_set.contains(3) == True
        assert intersection_set.contains('p') == True
        assert intersection_set.contains("{") == False

    def test_difference(self):
        new_set = Set(['l',1,2,3,'p'])
        other_set  = Set(['p',2,3,4])

        difference_set = new_set.difference(other_set)

        assert difference_set.contains(4) == True
        assert difference_set.contains('l') == True
        assert difference_set.contains('p') == False
        assert difference_set.contains("{") == False
        assert difference_set.size == 3

    def test_is_subset(self):
        new_set = Set(['l',1,2,3,'p',4])
        other_set  = Set(['p',1,2,3,4])

        assert new_set.is_subset(other_set) == True

        new_set = Set(['l',1,2,3,4])
        other_set  = Set(['p',1,2,3])

        assert new_set.is_subset(other_set) == False

        new_set = Set([2,3,4])
        other_set  = Set(['p',1,2,3])

        assert new_set.is_subset(other_set) == False


class CircularBufferTest(unittest.TestCase):

    def test__init__(self):
        cb = CircularBuffer(30)
        assert cb.max_size == 30
        assert cb.size == 0
        assert cb.container[0] == None


    def test_is_empty(self):
        cb = CircularBuffer(30)
        assert cb.is_empty() == True

    def test_is_full(self):
        cb = CircularBuffer(0)
        assert cb.is_full() == True

    def test_enqueue(self):
        cb = CircularBuffer(2)
        cb.enqueue(2)
        assert cb.is_full() == False
        cb.enqueue(3)
        assert cb.is_full() == True
        assert cb.size == 2
        assert cb.front() == 2


    def test_front(self):
        cb = CircularBuffer(1)
        cb.enqueue("hey")
        assert cb.front() == "hey"


    def test_dequeue(self):
        cb = CircularBuffer(2)
        cb.enqueue(2)
        cb.enqueue(3)
        cb.dequeue()
        assert cb.size == 1
        cb.dequeue()
        assert cb.is_empty() == True


    def test_pop(self):
        cb = CircularBuffer(4)
        cb.enqueue(2)
        cb.enqueue(3)
        cb.enqueue("A")
        cb.enqueue("B")
        cb.dequeue()
        cb.dequeue()
        cb.pop()
        cb.first == 2
        cb.last == 3
        cb.size == 1

if __name__ == '__main__':
    unittest.main()
