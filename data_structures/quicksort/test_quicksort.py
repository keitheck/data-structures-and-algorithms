from quicksort import quicksort


def test_quicksort_one():
    """Tests quicksort output return is correctly sorted."""
    assert quicksort([4, 7, 3, 6, 1, 10, 2, 5]) == [1, 2, 3, 4, 5, 6, 7, 10]


def test_quicksort_two():
    """Tests quicksort output return is correctly sorted."""
    assert quicksort([9567, 3472, 667, 200966, 34567, 87, 43334124, 2985, 287493, 245964, 1, 6, 903]) == [1, 6, 87, 667, 903, 2985, 3472, 9567, 34567, 200966, 245964, 287493, 43334124]


def test_quicksort_neg():
    """Test that quicksort handles negative integers."""
    assert quicksort([9567, 3472, 667, -200966, 34567, 87, 43334124, -2985, 287493, -245964, 1, 6, 903]) == [-245964, -200966, -2985, 1, 6, 87, 667, 903, 3472, 9567, 34567, 287493, 43334124]


def test_quicksort_float():
    """Tests that quicksort returns floats properly."""
    assert quicksort([1.01, 10.01, 100.10, 100.11, 1.1, 1.11, 100]) == [1.01, 1.1, 1.11, 10.01, 100, 100.1, 100.11]    
   

def test_quicksort_empty():
    """Tests that quicksort returns empty."""
    assert quicksort([]) == []


def test_quicksort_length_one():
    """Tests that quicksort returns length one."""
    assert quicksort([6]) == [6]