from .k_tree import Ktree
import pytest

@pytest.fixture
def height_one_tree():
    tree = Ktree(0, [])
    return tree


@pytest.fixture
def depth_one_tree():
    tree = Ktree(0)
    tree.root.children = [1,2,3,4]
    return tree

    
