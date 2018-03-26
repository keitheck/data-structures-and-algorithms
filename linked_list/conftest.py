import pytest
from node import Node
from linked_list import LinkedList as LLCONFTEST

@pytest.fixture
def empty_new_list():
    """test new linked list """
    return LLCONFTEST()


@pytest.fixture
def new_ll_iter():
    """test that accepts input of list"""
    return LLCONFTEST([1, 2, 3, 4])

@pytest.fixture
def new_ll_nested():
    """test insertion of nexted lists"""
    return LLCONFTEST([{1:1}, [2,2], 3, 'string'])

