# tests/test_my_module.py
from src.my_module import add, is_even

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
