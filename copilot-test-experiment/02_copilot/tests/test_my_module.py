# test_my_module.py
from src.my_module import add, is_even
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1000000, 2000000) == 3000000

# Test for the add function
def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False
    assert is_even(1000000) == True
    assert is_even(1000001) == False
    assert is_even(-1000000) == True
    assert is_even(-1000001) == False
    assert is_even(0.0) == True