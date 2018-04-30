from print_level_order import Ktree, print_level_order
import pytest


def test_empty_tree(height_one_tree):
    """test root val of single node tree"""
    assert height_one_tree.root.val is 0


def test_val_root_filled_tree(depth_one_tree):
    """test root of filled tree"""
    assert depth_one_tree.root.val is 0  


def test_children_tree(depth_one_tree):
    """test root of filled tree"""
    assert str(depth_one_tree.root.children) == str([1, 2, 3, 4])    


def test_preorder_traversal(depth_one_tree):
    """tests that pre-order traversal retruns corret nodes"""
    testlist = []
    depth_one_tree.pre_order(lambda x: testlist.append(x))
    assert str(testlist) == str([0, 1, 2, 3, 4])


def test_postorder_traversal(depth_one_tree):
    """tests that post-order traversal retruns corret nodes"""
    testlist = []
    depth_one_tree.post_order(lambda x: testlist.append(x))
    assert str(testlist) == str([1, 2, 3, 4, 0])


def test_breadth_first(depth_one_tree):
    """test that breadth first returns correct"""
    testlist = []
    depth_one_tree.breadth_first(lambda x: testlist.append(x))
    assert str(testlist) == str([0, 1, 2, 3, 4])


def test_inset(depth_one_tree):
    """tests that insert works as expected"""
    depth_one_tree.insert(2, 3)
    print(depth_one_tree.root.children[0].children)
    print(depth_one_tree.root.children[1].children)
    print(depth_one_tree.root.children[2].children)
    print(depth_one_tree.root.children[3].children)
    assert str(depth_one_tree.root.children[2].children) == str([2])


def test_print_level_order(depth_one_tree):
    """tests that depth one tree returns correctly"""
    assert print_level_order(depth_one_tree) == ['0', '1 2 3 4']


def test_print_level_order_2(depth_one_tree):
    """tests that depth one tree returns correctly"""
    depth_one_tree.insert(5, 1)
    depth_one_tree.insert(6, 2)
    depth_one_tree.insert(7, 3)
    depth_one_tree.insert(8, 4)
    assert print_level_order(depth_one_tree) == ['0', '1 2 3 4', '5 6 7 8']


def test_print_level_order():
    """tests typeerror of non-tree argument"""
    with pytest.raises(TypeError):
        print_level_order(1)
    with pytest.raises(TypeError):
        print_level_order('string')
    with pytest.raises(TypeError):
        print_level_order([1, 2, 3, 4])    