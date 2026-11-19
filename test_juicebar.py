"""Tests for the JuiceBar order price. Run:  pytest -v test_juicebar.py
You add your own tests at the end of this file, under YOUR TESTS.
"""
import pytest

from juicebar import bottle_price, order_price

# ---------------------------------------------------------------------------
# Tests from the development team.
# The developers of JuiceBar wrote these 5 tests before you came.
# All of them pass now. But maybe they do not test everything well.
# Do not delete them. You may make one of them stronger in Part C.
# ---------------------------------------------------------------------------
def test_team_bottle_price():
    assert bottle_price("S") == 40


def test_team_two_small():
    assert order_price(2, "S") == 80


def test_team_five_small():
    assert order_price(5, "S") == 200


def test_team_big_order():
    assert order_price(12, "S") == 430


def test_team_member_order():
    assert order_price(3, "S", member=True) == 105


# ---------------------------------------------------------------------------
# YOUR TESTS (Part A2, Part B and Part C). Write your new tests here.
# Write the expected value from the SPECIFICATION (worksheet, step A0),
# not from the code.
# The input of a test can come from the code. The expected value must
# always come from the specification.
# ---------------------------------------------------------------------------
# This is an example of a normal test. Replace the dots with real values.
#
#
# def test_my_first():
#     assert order_price(..., ...) == ...
#
# This is an example of a test for an input that must raise an error.
#
#
# def test_my_error():
#     with pytest.raises(ValueError):
#         order_price(..., ...)

def test_large_bottle():
    assert bottle_price("L") == 60

def test_invalid_size():
    with pytest.raises(ValueError):
        bottle_price("X")

def test_invalid_qty():
    with pytest.raises(ValueError):
        order_price(0, "S")

def test_coupon_discount():
    assert order_price(2, "S", coupon=True) == 72

def test_min_qty():
    assert order_price(1, "S") == 40

def test_max_qty():
    assert order_price(20, "S") == 750

def test_ten_bottles_discount():
    assert order_price(10, "S") == 350