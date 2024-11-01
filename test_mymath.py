import pytest

from mymath import *

def test_add():
    assert add(3,4, 5) == 12

def test_subtract():
    assert subtract(3, 4, 5) == -6

def test_multiply():
    assert multiply(3, 4, 5) == 60

def test_divide():
    assert divide(3, 4, 5) == 0.15
    assert divide(4, 5, 6) == pytest.approx(0.13333, abs=0.00001)

def test_power():
    assert power(3, 2) == 9
    assert power(2, 3) == 8
    assert power(4, 4) == 256

def test_mod():
    assert mod(7, 4) == 3
    assert mod(7, 2) == 1
    assert mod(7, 5) == 2
