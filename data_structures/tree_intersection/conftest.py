from bst import BST
import pytest


@pytest.fixture
def short_depth():
    """a small bst with a depth of 2"""
    x = [10, 5, 15, 9, 16]
    bst = BST()
    for i in x:
        bst.insert(i)
    return bst


@pytest.fixture
def medium_depth():
    """a bst with several levels of depth"""
    x = [10, 5, 3, 7, 2, 4, 6, 8, 16, 12, 11, 13, 17, 16, 18]
    bst = BST()
    for i in x:
        bst.insert(i)
    return bst


@pytest.fixture
def long_depth():
    """a bst with several levels of depth"""
    x = [6, 5, 7, 7, 2, 4, 6, 8, 16, 12, 10, 13, 17, 17, 6]
    bst = BST()
    for i in x:
        bst.insert(i)
    return bst