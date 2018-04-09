import pytest


def test_insert_into_empty(empty_root):
    """add single node to empty bst"""
    empty_root.insert(10)
    assert empty_root.root.val == 10


def test_insert_into_empty_false_value(empty_root):
    """add a string to empty bst"""
    with pytest.raises(TypeError):
        assert empty_root.insert('shoe')
    

def test_insert_order_empty(empty_root):
    """test insertion order correct"""
    x = []
    empty_root.in_order_traversal(lambda i: x.append(str(i.val)))

    assert ''.join(x) == ''  


def test_insert_into_empty2(empty_root):
    """test correct insertion on an empty bst"""
    insert = [2, 1, 3]
    for i in insert:
        empty_root.insert(i)
    assert empty_root.root.val == 2
    assert empty_root.root.left.val == 1
    assert empty_root.root.right.val == 3


def test_short_depth_fixture(short_depth):
    """test short depth fixture is as expected"""
    assert short_depth.root.val == 10
    assert short_depth.root.left.val == 5
    assert short_depth.root.right.val == 15


def test_insertion_short_depth(short_depth):
    """tests proper insertion on short depth insert"""
    short_depth.insert(6)
    assert short_depth.root.left.right.val == 6    
    assert short_depth.root.left.left is None


def test_insertion_short_depth_2(short_depth):
    """tests proper insertion on short depth insert"""
    short_depth.insert(1)
    assert short_depth.root.left.right is None    
    assert short_depth.root.left.left.val == 1   


def test_insertion_short_depth_3(short_depth):
    """tests proper insertion on short depth insert"""
    short_depth.insert(11)
    assert short_depth.root.right.right is None    
    assert short_depth.root.right.left.val == 11


def test_insertion_short_depth_4(short_depth):
    """tests proper insertion on short depth insert"""
    short_depth.insert(33)
    assert short_depth.root.right.right.val == 33    
    assert short_depth.root.right.left is None


def test_repr(short_depth):
    """test repr"""
    assert short_depth.__repr__() == '<leaf vals => root: 10 | Left: 5 | Right: 15'


def test_str(short_depth):
    """test str"""
    assert short_depth.__str__() == 'root. val => 10'


def test_medium_depth(medium_depth):
    """tests medium depth fixture is as expected"""
    assert medium_depth.root.val == 10
    assert medium_depth.root.left.val == 5
    assert medium_depth.root.right.val == 15


def test_insert_meduim_depth(medium_depth):
    """tests insert into deepter search tree"""
    medium_depth.insert(13) 
    assert medium_depth.root.right.left.right.right.val == 13  


def test_n_order_traversal_short_depth(short_depth):
    """test in order method"""
    x = []
    short_depth.in_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '51015'


def test_n_order_traversal_medium_depth(medium_depth):
    """test in order method"""
    x = []
    medium_depth.in_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '23456781011121315161718'   


def test_pre_order_traversal_short_depth(short_depth):
    """test pre-order"""
    x = []
    short_depth.pre_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '10515'


def test_pre_order_traversal_medium_depth(medium_depth):
    """test pre-order"""
    x = []
    medium_depth.pre_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '10532476815121113171618'


def test_post_order_traversal_short_depth(short_depth):
    """test post-order"""
    x = []
    short_depth.post_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '51510'


def test_post_order_traversal_medium_depth(medium_depth):
    """test post-order"""
    x = []
    medium_depth.post_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '24368751113121618171510' 


    