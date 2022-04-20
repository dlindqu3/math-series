import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_1(): 
  actual = fibonacci(1)
  expected = 0
  assert actual == expected 

def test_fibonacci_2(): 
  actual = fibonacci(2)
  expected = 1
  assert actual == expected 

def test_fibonacci_3(): 
  actual = fibonacci(3)
  expected = 1
  assert actual == expected 

def test_fibonacci_8(): 
  actual = fibonacci(8)
  expected = 13
  assert actual == expected 

def test_lucas_1(): 
  actual = lucas(1)
  expected = 2
  assert actual == expected 

def test_lucas_1(): 
  actual = lucas(1)
  expected = 2
  assert actual == expected 

def test_lucas_1(): 
  actual = lucas(5)
  expected = 7
  assert actual == expected 

def test_sum_series_1f(): 
  actual = sum_series(1)
  expected = 0 
  assert actual == expected

def test_sum_series_2f(): 
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_sum_series_5f(): 
  actual = sum_series(5)
  expected = 3
  assert actual == expected

def test_sum_series_1l(): 
  actual = sum_series(3, 2, 1)
  expected = 3
  assert actual == expected


def test_sum_series_5l(): 
  actual = sum_series(5, 2, 1)
  expected = 7
  assert actual == expected