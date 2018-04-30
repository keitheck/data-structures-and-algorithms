from hash_table import HashTable
import pytest 

@pytest.fixture
def empty_HT():
    hash_table = HashTable()
    return hash_table