# test_tasks.py

import pytest
from main import square_properties, rectangle_properties, financial_planning

def test_square_properties():
    perimeter, area = square_properties(6)
    assert perimeter == 24
    assert area == 36

def test_rectangle_properties():
    perimeter, area = rectangle_properties(5, 7)
    assert perimeter == 24
    assert area == 35

@pytest.mark.parametrize("salary, mortgage_percent, life_percent, expected_mortgage, expected_life, expected_savings", [
    (100000, 30, 50, 360000, 600000, 240000),
    (120000, 25, 40, 360000, 576000, 504000)
])
def test_financial_planning(salary, mortgage_percent, life_percent, expected_mortgage, expected_life, expected_savings):
    mortgage, life, savings = financial_planning(salary, mortgage_percent, life_percent)
    assert mortgage == expected_mortgage
    assert life == expected_life
    assert savings == expected_savings

