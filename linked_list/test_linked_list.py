from linked_list import LinkedList as ll
import pytest as pytest


def test_init__(empty_new_list):
    """test insert into empty list"""
    empty_new_list.insert(1)
    assert empty_new_list.head.val == 1

   
def test_init_multiple(empty_new_list):
    """test insert multipe into empty list"""
    empty_new_list.insert(1)
    empty_new_list.insert(2)
    empty_new_list.insert(3)
    assert empty_new_list.head.val == 3 


def test_init_with_list(new_ll_iter):
    """test linked list with init"""
    assert len(new_ll_iter) is 4


def test_init_with_list_head_value(new_ll_iter):
    """test linked list with init proper head value"""   
    assert new_ll_iter.head.val == 1


def test_init_with_iter_add_node(new_ll_iter):
    """test adding node to new LL created with list"""
    assert len(new_ll_iter) is 4
    new_ll_iter.insert('a')
    assert new_ll_iter.head.val == 'a'
    assert len(new_ll_iter) is 5
    assert new_ll_iter.head._next.val == 1


def test_nested_instantiation(new_ll_nested):
    """test instantiation with nested data types"""
    assert new_ll_nested.head.val == {1:1}
    assert new_ll_nested.head._next.val == [2,2]
    assert new_ll_nested.head._next._next.val == 3
    assert new_ll_nested.head._next._next._next.val == 'string'


def test_empty_list_is_empty(empty_new_list):
    """istantiation of empty list is empty"""
    assert len(empty_new_list) == 0


def test_magic_len_(new_ll_iter):
    """test __len__"""
    assert new_ll_iter.__len__() == 4

