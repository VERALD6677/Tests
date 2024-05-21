# main.py

def square_properties(a):
    """Returns the perimeter and area of a square with side length a."""
    perimeter = a * 4
    area = a ** 2
    return perimeter, area

def rectangle_properties(a, b):
    """Returns the perimeter and area of a rectangle with sides a and b."""
    perimeter = 2 * (a + b)
    area = a * b
    return perimeter, area

def financial_planning(salary, mortgage_percent, life_percent):
    """Calculates the mortgage, life expenses and savings for a given salary."""
    mortgage = (salary * mortgage_percent / 100) * 12
    life = (salary * life_percent / 100) * 12
    savings = (salary * 12) - mortgage - life
    return mortgage, life, savings
