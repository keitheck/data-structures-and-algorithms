from breadth_first_traversal import breadthFirstTraversal as bft


def test_empty(test_empty_tree):
    """tests empty tree returns false"""
    assert bft(test_empty_tree) == []


def test_medium(test_medium_tree):
    """tests medium size tree"""
    assert bft(test_medium_tree) == [10, 5, 15, 3, 6, 14, 16]


def test_large(test_large_tree):
    """tests large size tree"""
    assert bft(test_large_tree) == [10, 5, 15, 3, 9, 14, 4567, 1, 6, 9, 55, 12334, 16, 77, 24]    