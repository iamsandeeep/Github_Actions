import pytest
from calc import add, subtract, multiply, divide

def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(10, 5) == 2.0

def test_divide_by_zero():
    assert divide(10, 0) == "Error! Division by zero."
