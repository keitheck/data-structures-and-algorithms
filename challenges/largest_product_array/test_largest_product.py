import largest_product


def test_product_returns():
    # test if returns a single product
    assert largest_product.largest([[2, 2]]) is 4
    

def test_returns_largest():    
    # test if returns the largest of longer array
    assert largest_product.largest([[3, 4], [5, 8], [1, 2]]) is 40


def test_empty_list():    
    # test if returns msg if empty list
    assert largest_product.largest([]) == 'empty list used' 

