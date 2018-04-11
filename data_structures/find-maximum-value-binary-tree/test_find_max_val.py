from find_maximum_value_binary_tree import find_maximum_value as find


def test_empty(test_empty_tree):
    """tests empty tree returns false"""
    assert find(test_empty_tree) == False


def test_medium(test_medium_tree):
    """tests medium size tree"""
    assert find(test_medium_tree) == 16


def test_large(test_large_tree):
    """tests large size tree"""
    assert find(test_large_tree) == 12334