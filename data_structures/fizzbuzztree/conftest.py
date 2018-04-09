from fizzbuzztree import fizzbuzztree
from bst import BST
import pytest


@pytest.fixture
def empty_root():
    """returns and empty searc tree"""
    return BST()


@pytest.fixture
def short_depth():
    """a small bst with a depth of 2"""
    x = [10, 3, 15, 4]
    bst = BST()
    for i in x:
        bst.insert(i)
    return bst


@pytest.fixture
def medium_depth():
    """a bst with several levels of depth"""
    x = [10, 5, 3, 7, 2, 4, 6, 8, 15, 12, 11, 13, 17, 16, 18]
    bst = BST()
    for i in x:
        bst.insert(i)
    return bst

