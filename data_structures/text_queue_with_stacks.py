from queue_with_stacks import Queue_with_stacks as ST
import pytest


def test_init(empty_stack):
    """initiate with no value"""
    teststack = ST(empty_stack)
    assert teststack.stack_back.top.val is None


def test_init(iter_stack):
    """initiate with value"""
    teststack = ST(iter_stack)
    assert teststack.stack_back.top.val == 5   


def test_init(iter_stack):
    """initiate with value stack front"""
    teststack = ST(iter_stack)
    assert teststack.stack_front.top.val in None 


# def test_empty_stack_has_no_top(empty_stack):
#     assert empty_stack.top is None


# def test_insertion(empty_stack):
#     assert empty_stack.top is None
#     assert empty_stack.push(1).val == 1


# def test_empty_val_on_insert(empty_stack):
#     with pytest.raises(TypeError):
#         empty_stack.push()