import binary_search as binary
# import pytest as pytest


def test_find_index():
    # test is key is in list
    assert binary.binary_search([1, 2, 3, 4, 5], 5) is 4


def test_not_in_list():    
    # test that key is not in list
    assert binary.binary_search([22, 34, 55, 67, 89, 320, 675, 12233], 11) is -1
    sample_list = list(range(3, 100000, 13))
    assert binary.binary_search([sample_list], 4557) is -1


def test_empty_list():    
    # test that list is empty
    assert binary.binary_search([], 1) is -1

