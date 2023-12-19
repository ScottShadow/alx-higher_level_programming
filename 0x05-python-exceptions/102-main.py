#!/usr/bin/python3
magic_calculation = __import__('102-magic_calculation').magic_calculation


def main():
    # Sample values
    a_value = 5
    b_value = 2

    # Call magic_calculation function
    result = magic_calculation(a_value, b_value)

    # Display the result
    print(
        f"The result of magic_calculation({a_value}, {b_value}) is: {result}")


if __name__ == "__main__":
    main()
