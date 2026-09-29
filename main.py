from arithmetic import (
    addition,
    subtraction,
    multiplication,
    division
)

from number_analysis import (
    is_prime,
    is_armstrong,
    is_palindrome,
    is_even,
    is_perfect
)

from advanced_math import (
    factorial,
    power,
    gcd,
    lcm,
    fibonacci
)

from input_handler import (
    get_numbers,
    get_multiple_numbers,
    get_integer
)

from calculator_utils import (
    display_title,
    display_menu
)


def main():

    display_title()

    while True:

        try:

            display_menu()

            choice = input("Enter your choice: ").strip()

            

            if choice == "1":

                numbers = get_multiple_numbers()

                result = addition(numbers)

                print(f"Result: {result}")

            elif choice == "2":

                numbers = get_multiple_numbers()

                result = subtraction(numbers)

                print(f"Result: {result}")

            elif choice == "3":

                a, b = get_numbers()

                result = multiplication(a, b)

                print(f"Result: {result}")

            elif choice == "4":

                a, b = get_numbers()

                result = division(a, b)

                print(f"Result: {result}")

            

            elif choice == "5":

                n = get_integer(
                    "Enter an integer: "
                )

                if is_prime(n):
                    print(
                        f"{n} is a Prime Number."
                    )
                else:
                    print(
                        f"{n} is not a Prime Number."
                    )

            elif choice == "6":

                n = get_integer(
                    "Enter an integer: "
                )

                if is_armstrong(n):
                    print(
                        f"{n} is an Armstrong Number."
                    )
                else:
                    print(
                        f"{n} is not an Armstrong Number."
                    )

            elif choice == "7":

                n = get_integer(
                    "Enter an integer: "
                )

                if is_palindrome(n):
                    print(
                        f"{n} is a Palindrome Number."
                    )
                else:
                    print(
                        f"{n} is not a Palindrome Number."
                    )

            elif choice == "8":

                n = get_integer(
                    "Enter an integer: "
                )

                if is_even(n):
                    print(
                        f"{n} is Even."
                    )
                else:
                    print(
                        f"{n} is Odd."
                    )

            elif choice == "9":

                n = get_integer(
                    "Enter an integer: "
                )

                if is_perfect(n):
                    print(
                        f"{n} is a Perfect Number."
                    )
                else:
                    print(
                        f"{n} is not a Perfect Number."
                    )


            elif choice == "10":

                n = get_integer(
                    "Enter a non-negative integer: "
                )

                if n < 0:

                    print(
                        "Invalid input. "
                        "Factorial is not defined "
                        "for negative numbers."
                    )

                else:

                    result = factorial(n)

                    print(
                        f"Factorial of {n}: {result}"
                    )

            elif choice == "11":

                a, b = get_numbers()

                result = power(a, b)

                print(
                    f"{a} raised to the power {b} = {result}"
                )

            elif choice == "12":

                a = get_integer(
                    "Enter first integer: "
                )

                b = get_integer(
                    "Enter second integer: "
                )

                result = gcd(a, b)

                print(
                    f"GCD of {a} and {b}: {result}"
                )

            elif choice == "13":

                a = get_integer(
                    "Enter first integer: "
                )

                b = get_integer(
                    "Enter second integer: "
                )

                result = lcm(a, b)

                print(
                    f"LCM of {a} and {b}: {result}"
                )

            elif choice == "14":

                n = get_integer(
                    "Enter the position: "
                )

                if n < 0:

                    print(
                        "Invalid input. "
                        "Fibonacci position "
                        "cannot be negative."
                    )

                else:

                    result = fibonacci(n)

                    print(
                        f"Fibonacci({n}) = {result}"
                    )

            

            elif choice == "15":

                print()
                print(
                    "Thank you for using "
                    "Smart Calculator!"
                )
                print("Goodbye!")

                break

          

            else:

                print(
                    "Invalid input. "
                    "Please select a valid option."
                )

            print()

        except ZeroDivisionError:

            print(
                "Invalid input. "
                "Cannot divide by zero."
            )

            print()

        except ValueError as error:

            print(
                f"Invalid input. {error}"
            )

            print()

        except Exception:

            print(
                "Invalid input. "
                "Please try again."
            )

            print()


if __name__ == "__main__":
    main()