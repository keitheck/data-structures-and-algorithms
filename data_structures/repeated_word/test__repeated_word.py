import pytest
from repeated_word import repeated_word


def test_string_validation():
    """test string validation returns TypeError"""
    with pytest.raises(TypeError):
        repeated_word([1, 2, 3])
    with pytest.raises(TypeError):
        repeated_word(9)    
    with pytest.raises(TypeError):
        repeated_word({'string': 'value'})


def test_short_string():
    """tests return duplcate with short string"""
    string = 'one two three two seven'
    assert repeated_word(string) == 'two'


def test_long_string():
    """tests return duplcate with longer string"""
    string = 'I like to eat apples and bananas great bananas apple'
    assert repeated_word(string) == 'bananas'


def test_no_match():
    """tests return no match in string"""
    string = 'I like to eat eight apples and bananas'
    assert repeated_word(string) == 'No duplicate words found'
