def factorial(n):
    """Calculate factorial of a non-negative integer."""

    if n < 0:
        raise ValueError(
            "Factorial is not defined for negative numbers."
        )

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def power(a, b):
    """Calculate a raised to the power b."""

    return a ** b


def gcd(a, b):
    """Calculate the Greatest Common Divisor."""

    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    """Calculate the Least Common Multiple."""

    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


def fibonacci(n):
    """Return the nth Fibonacci number."""

    if n < 0:
        raise ValueError(
            "Fibonacci position cannot be negative."
        )

    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b