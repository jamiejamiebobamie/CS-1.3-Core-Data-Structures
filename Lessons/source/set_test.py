from set import Set
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



if __name__ == '__main__':
    unittest.main()
