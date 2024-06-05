import pytest
from functions.helpers import normalize_string
import re


def test_removes_non_alphanumeric_characters():
    assert normalize_string("Hello, World!") == "hello_world"

if __name__ == "__main__":
    pytest.main()