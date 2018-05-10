from radix_sort import radix_sort, place_value, array_buckets, sorted_list
import pytest


def test_place_value():
    """test that proper digit is returned"""
    assert place_value(1234, 0) == 4
    assert place_value(1234, 1) == 3
    assert place_value(1234, 2) == 2
    assert place_value(1234, 3) == 1


def test_array_buckets():
    """tests helper places numbers into proper buckets"""
    assert array_buckets([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 0) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]] 


def test_array_buckets_two():
    """tests helper places similar digit place values into proper buckets"""
    assert array_buckets([1, 11, 42, 111, 482], 0) == [[], [1, 11, 111], [42, 482], [], [], [], [], [], [], []] 


def test_sorted_list(return_filled_buckets):
    """tests that buckets output properly to new list"""
    # assert sorted_list(return_filled_buckets) == []
    buckets = return_filled_buckets
    assert sorted_list(buckets) == [1, 11, 111, 21, 42, 482, 543, 34, 9876, 9]


def test_sorted_list_two(return_filled_buckets):
    """tests that buckets output properly to new list"""
    # assert sorted_list(return_filled_buckets) == []
    buckets = return_filled_buckets
    sort1 = sorted_list(buckets)    
    buckets = array_buckets(sort1, 1)
    sort2 = sorted_list(buckets)
    buckets = array_buckets(sort2, 2)
    sort3 = sorted_list(buckets)
    buckets = array_buckets(sort3, 3)
    assert sorted_list(buckets) == [1, 9, 11, 21, 34, 42, 111, 482, 543, 9876]


def test_radix_sort_one():
    """test returns expected"""
    assert radix_sort([1, 11, 42, 111, 482, 9, 9876, 543, 21, 34]) == [1, 9, 11, 21, 34, 42, 111, 482, 543, 9876]

  