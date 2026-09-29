def addition(numbers):
    """Add multiple numbers."""
    result = 0

    for number in numbers:
        result += number

    return result


def subtraction(numbers):
    """Subtract multiple numbers from the first number."""
    result = numbers[0]

    for number in numbers[1:]:
        result -= number

    return result


def multiplication(a, b):
    """Multiply two numbers."""
    return a * b


def division(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b