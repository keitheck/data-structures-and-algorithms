import binary_search as binary_search
import pytest as pytest


def test_find_index():
    # test is key is in list
    assert binary_search.find_index([1, 2, 3, 4, 5], 5) is 4
    # test that key is not in list
    assert binary_search.find_index([22, 34, 55, 67, 89, 320, 675, 12233], 11) is -1
    # test that list is empty
    assert binary_search.find_index([], 1) is -1
    sample_list = list(range(3, 100000, 13))
    assert binary_search.find_index([sample_list], 4557) is -1
    

