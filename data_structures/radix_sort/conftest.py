from radix_sort import radix_sort, place_value, array_buckets, sorted_list
import pytest


@pytest.fixture
def return_filled_buckets():
    return array_buckets([1, 11, 42, 111, 482, 9, 9876, 543, 21, 34], 0)
