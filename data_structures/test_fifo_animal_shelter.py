from fifo_animal_shelter import AnimalShelter as ASH
import pytest


def test_init(test_ASH_inits):
    """initiate with no value"""
    a = test_ASH_inits
    assert a.stack_back.__len__() == 0


# def test_init_two():
#     """initiate with value"""
#     teststack2 = ST([1, 2, 3, 4, 5])
#     assert teststack2.stack_back.top.val == 1   


# def test_init_three(iter_stack):
#     """initiate with value stack front"""
#     assert iter_stack.stack_front.top is None
#     pass


# def test_enqueue(empty_stack):
#     """enqueue with empty stack"""
#     empty_stack.enqueue(1)
#     assert empty_stack.stack_back.top.val == 1


# def test_enqueue_two(empty_stack):
#     """enqueue two with empty stack"""
#     empty_stack.enqueue(1)
#     empty_stack.enqueue(2)
#     assert empty_stack.stack_back.top.val == 2   


# def test_enqueue(empty_stack):
#     """enqueue multiple with empty stack"""
#     empty_stack.enqueue(1)
#     empty_stack.enqueue(2)
#     empty_stack.enqueue(3)
#     assert empty_stack.stack_back.top.val == 3 


# def test_dequeue(empty_stack):
#     """test dequeue returns first in"""
#     empty_stack.enqueue(1)
#     empty_stack.enqueue(2)
#     empty_stack.enqueue(3)
#     assert empty_stack.dequeue() == 1   


# def test_dequeue(empty_stack):
#     """test dequeue returns first in string value"""
#     empty_stack.enqueue('a')
#     empty_stack.enqueue('b')
#     empty_stack.enqueue('c')
#     assert empty_stack.dequeue() == 'a'   


# def test_dequeue(empty_stack):
#     """test dequeue returns first in list value"""
#     empty_stack.enqueue([1, 2])
#     empty_stack.enqueue([3, 4])
#     empty_stack.enqueue([5, 6])
#     assert empty_stack.dequeue() == [1, 2]     