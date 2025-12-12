from calculator import (
    calculate_compound_interest,
    calculate_simple_interest,
    calculate_tax,
)
from pytest import approx
import pytest


def test_calculate_simple_interest():
    assert calculate_simple_interest(0, 0, 0) == approx(0.0)
    assert calculate_simple_interest(10, 10, 10) == approx(10.0)
    with pytest.raises(ValueError):
        calculate_simple_interest(-1, -1, -1)


def test_calculate_compound_interest():
    assert calculate_compound_interest(0, 0, 0, 1) == approx(0.0)
    assert calculate_compound_interest(10, 10, 10, 2) == approx(26.53297)
    with pytest.raises(ValueError):
        calculate_compound_interest(-1, -1, -1, 2)
    with pytest.raises(ValueError):
        calculate_compound_interest(10, 1.2, 10, 0)


def test_calculate_tax():
    assert calculate_tax(0, 0) == approx(0.0)
    assert calculate_tax(100, 30) == approx(30.0)
    with pytest.raises(ValueError):
        calculate_tax(-2, 80)
    with pytest.raises(ValueError):
        calculate_tax(0, 120)
