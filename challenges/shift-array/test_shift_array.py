import shift_array as sa


def test_new_list_inserts_correctly_even():
    """test if new linked list is correctly created"""
    assert sa.new_list([2, 3, 4, 5], 6) == [2, 3, 6, 4, 5]


def test_new_list_inserts_correctly_odd():
    """test if new linked list is correctly created"""
    assert sa.new_list([2, 3, 4, 5, 6], 7) == [2, 3, 4, 7, 5, 6]  


def test_insert_non_int():
    """test if new linked list is correctly created with different data types"""
    assert sa.new_list([1, 2, 3, 4, 5, 6], 'a') == [1, 2, 3, 'a', 4, 5, 6]   