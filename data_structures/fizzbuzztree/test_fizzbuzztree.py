import pytest
from fizzbuzztree import fizzbuzztree as fbt


def test_empty(empty_root):
    """test returns message if tree is empty"""
    assert fbt(empty_root) == 'Tree is empty. Please use a populated tree of integers'


def test_short_depth(short_depth):
    """tests short depth tree"""
    fbt(short_depth)
    assert str(short_depth.root.val) == 'buzz'


def test_short_depth2(short_depth):
    fbt(short_depth)
    assert str(short_depth.root.left.val) == 'fizz'


def test_short_depth3(short_depth):
    fbt(short_depth)
    assert str(short_depth.root.right.val) == 'fizzbuzz'  


def test_short_depth4(short_depth):
    fbt(short_depth)
    assert str(short_depth.root.left.right.val) == '4'    


def test_medium_depth(medium_depth):
    fbt(medium_depth)
    x = []
    medium_depth.in_order_traversal(lambda i: x.append(str(i.val)))
    assert ''.join(x) == '2fizz4buzzfizz78buzz11fizz13fizzbuzz1617fizz'

