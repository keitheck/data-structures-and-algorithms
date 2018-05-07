from left_join import left_join
import pytest
import pdb


def test_hash_key(insert_hash):
    """test hash_tables returns expexted string values."""
    ht = insert_hash
    ht2 = insert_hash
    ht.set('desk', 'table')
    ht.set('chair', 'stool')
    ht2.set('desk', 'counter')
    ht2.set('chair', None)
    assert ht.get('a') == 'aa'
    assert ht.get('CodeFellows') == 'school'
    assert ht2.get('desk') == 'counter'


def test_hash_return_key(insert_hash):
    """tests that return_key functions as expected"""
    ht = insert_hash
    # assert ht.return_k_v() == []
    assert ht.return_k_v() == ['CodeFellows', 'a']    


def test_left_join1(insert_hash, insert_hash2):
    """tests that return_key functions as expected"""
    ht = insert_hash
    ht2 = insert_hash2
    new = left_join(ht2, ht)
    assert new.return_k_v() == ['CodeFellows', 'b', 'tree']


def test_left_join2(insert_hash, insert_hash2):
    """tests that left_join functions as expected"""
    ht = insert_hash
    ht2 = insert_hash2
    new = left_join(ht2, ht)
    assert new.get('b') == ['bb', None]


def test_left_join3(insert_hash, insert_hash2):
    """tests that left_join handles table 2 with no matchging key"""
    ht = insert_hash
    ht2 = insert_hash2
    new = left_join(ht2, ht)
    assert new.get('tree') == ['shrub', None]


def test_left_join_type(insert_hash):
    """confirms TypeError exception"""
    with pytest.raises(TypeError): 
        assert left_join(insert_hash, 'string') 
