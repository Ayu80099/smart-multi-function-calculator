def is_prime(n):
    """Check whether a number is prime."""

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_armstrong(n):
    """Check whether a number is an Armstrong number."""

    if n < 0:
        return False

    digits = str(n)
    power = len(digits)

    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == n


def is_palindrome(n):
    """Check whether a number is a palindrome."""

    if n < 0:
        return False

    number = str(n)

    return number == number[::-1]


def is_even(n):
    """Check whether a number is even."""

    return n % 2 == 0


def is_perfect(n):
    """Check whether a number is a perfect number."""

    if n <= 1:
        return False

    total = 1

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            total += i

            if i != n // i:
                total += n // i

    return total == n