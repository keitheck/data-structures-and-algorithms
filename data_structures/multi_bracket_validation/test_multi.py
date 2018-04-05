from .multi_bracket_validation import multi_bracket_validation as multi
from stack.stack import Stack as ST
import pytest


def test_short_string():
    assert multi('(fd)') == True


def test_long_string():
    assert multi('()dsfdsa{vde[]ds}') == True


def test_false():
    assert multi('[{dfrr{daf){(}}}') == False    


def test_false_2():
    assert multi(')') == False