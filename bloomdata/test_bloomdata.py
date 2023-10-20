''' This is to test the bloomdata file'''
import pytest
from bloomdata import bloomdata as bd

def test_increment_int():
    assert bd.increment(3) == 4

def test_increment_float():
    assert bd.increment(1.5) == 2.5

def test_increment_return_type():
    assert isinstance(bd.increment(3), int)
