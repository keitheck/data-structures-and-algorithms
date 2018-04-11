from breadth_first_traversal import breadthFirstTraversal as bft


def test_empty(test_empty_tree):
    """tests empty tree returns false"""
    assert bft(test_empty_tree) is False


def test_medium(test_medium_tree):
    """tests medium size tree"""
    assert bft(test_medium_tree)