from datastructures.intervaltree import IntervalTree

class TestIntervalTree:
    def test_search(self):
        tree=IntervalTree()
        
        tree.insert(100,150, 'apple')
        tree.insert(150,175, 'microsoft')
        tree.insert(120,160, 'tesla')
        tree.insert(200,250, 'google')

        assert tree.search(125) == {'apple', 'tesla'}

    def test_range_search(self):
        tree=IntervalTree()
        
        tree.insert(100,150, 'apple')
        tree.insert(150,175, 'microsoft')
        tree.insert(120,160, 'tesla')
        tree.insert(200,250, 'google')
        tree.insert(100,200, 'amazon')

        assert tree.range_search(130, 165) == {'amazon','apple', 'tesla', 'microsoft'}