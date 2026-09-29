def get_numbers():
    """Get two numbers from the user."""

    while True:

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            return a, b

        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def get_multiple_numbers():
    """Get multiple numbers from the user."""

    while True:

        try:

            count = int(
                input("How many numbers do you want to enter? ")
            )

            if count < 2:
                print(
                    "Invalid input. Please enter at least 2 numbers."
                )
                continue

            numbers = []

            for i in range(count):

                while True:

                    try:

                        number = float(
                            input(f"Enter number {i + 1}: ")
                        )

                        numbers.append(number)

                        break

                    except ValueError:

                        print(
                            "Invalid input. Please enter a valid number."
                        )

            return numbers

        except ValueError:

            print(
                "Invalid input. Please enter a valid number."
            )


def get_integer(prompt):
    """Get a valid integer from the user."""

    while True:

        try:

            return int(input(prompt))

        except ValueError:

            print(
                "Invalid input. Please enter a valid integer."
            )