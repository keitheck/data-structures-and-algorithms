import pytest
from bst import BST


@pytest.fixture
def test_empty_tree():
    """returns empty tree"""
    return BST()


@pytest.fixture
def test_medium_tree():
    """returns medium tree""" 
    l = [10, 5, 15, 3, 6, 14, 16]
    tree = BST()
    for i in l:
        tree.insert(i)  
    return tree


@pytest.fixture
def test_large_tree():
    """returns large tree"""
    l = [10, 5, 15, 9, 3, 4567, 55, 6, 1, 12334, 14, 16, 77, 24, 9]
    tree = BST()
    for i in l:
        tree.insert(i)  
    return tree