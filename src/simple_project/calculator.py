import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square_root(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)


def power(a, b):
    """Return a raised to the power of b."""
    return math.pow(a, b)


def sine(a):
    """Return the sine of a (in radians)."""
    return math.sin(a)


def cosine(a):
    """Return the cosine of a (in radians)."""
    return math.cos(a)


def tangent(a):
    """Return the tangent of a (in radians)."""
    return math.tan(a)


def logarithm(a, base=math.e):
    """Return the logarithm of a with the given base."""
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(a, base)
