# from queue_with_stacks import Queue_with_stacks
# from fifo_animal_shelter import AnimalShelter as ASH
# import pytest


# @pytest.fixture
# def test_AHS_inits():
#     return ASH()


# @pytest.fixture
# def empty_stack():
#     return Queue_with_stacks()


# @pytest.fixture
# def iter_stack():
#     return Queue_with_stacks([1, 2, 3, 4, 5])    


# @pytest.fixture
# def small_stack():
#     s = Queue_with_stacks()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.push(5)
#     return s


# @pytest.fixture
# def large_stack():
#     s = Queue_with_stacks()

#     for num in range(1000):
#         s.push(num)

#     return s