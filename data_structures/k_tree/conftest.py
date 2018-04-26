from .k_tree import Ktree
import pytest

@pytest.fixture
def height_one_tree():
    """returns tree with only root"""
    tree = Ktree(0, [])
    return tree


@pytest.fixture
def depth_one_tree():
    """returns tree with root and children nodes"""
    tree = Ktree(0, [1, 2, 3, 4])
    # tree.root.children = [1, 2, 3, 4]
    return tree

    
@pytest.fixture
def insert_into_empty():
    """returns tree insert as child of root"""
    tree = Ktree(1, [])
    tree.insert(1, 2)
    return tree


@pytest.fixture
def insert_at_depth():
    """retu
    rns tree with multiple inserts"""
    tree = Ktree(1, [])
    tree.root.children = [2, 3, 4, 5]
    tree.insert(2, 6)
    tree.insert(5, 7)
    tree.insert(7, 8)
    return tree    
