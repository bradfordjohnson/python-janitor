import pytest
from functions.helpers import normalize_string
import re


def test_removes_non_alphanumeric_characters():
    assert normalize_string("Hello, World!") == "hello_world"

def test_multiple_spaces():
    assert normalize_string("Hello,  World!") == "hello_world"

def test_numbers_in_front_of_string():
    assert normalize_string("123abc") == "123_abc"

def test_numbers_behind_string():
    assert normalize_string("abc123") == "abc_123"
    
def test_numbers_in_middle_of_string():
    assert normalize_string("ab123c") == "ab_123_c"
    
if __name__ == "__main__":
    pytest.main()