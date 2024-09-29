# Define the functions for the calculator
from constants import ENTER_FIRST_NUMBER, ENTER_SECOND_NUMBER, ENTER_CHOICE, RESULT_IS, INVALID_INPUT, SELECT_OPERATION, \
    ADD_OPTION, SUBTRACT_OPTION, MULTIPLY_OPTION, DIVIDE_OPTION


def add(x, y):
    """
    Add two numbers and return the result.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The sum of x and y
    """
    return x + y


def subtract(x, y):
    """
    Subtract second number from the first and return the result.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The difference between x and y
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers and return the result.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float: The product of x and y
    """
    return x * y


def divide(x, y):
    """
    Divide the first number by the second and return the result.

    Parameters:
    x (float): First number
    y (float): Second number

    Returns:
    float or str: The quotient of x and y or an error message if division by zero is attempted.
    """
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Main program
def calculator():
    """
    Calculator program that performs basic arithmetic operations.
    Allows the user to select an operation, input two numbers, and receive the result.
    """

    print(SELECT_OPERATION)
    print(ADD_OPTION)
    print(SUBTRACT_OPTION)
    print(MULTIPLY_OPTION)
    print(DIVIDE_OPTION)

    choice = input(ENTER_CHOICE)

    if choice in ['1', '2', '3', '4']:
        num1 = float(input(ENTER_FIRST_NUMBER))
        num2 = float(input(ENTER_SECOND_NUMBER))

        if choice == '1':
            print(f"{RESULT_IS}: {add(num1, num2)}")
        elif choice == '2':
            print(f"{RESULT_IS}: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{RESULT_IS}: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{RESULT_IS}: {divide(num1, num2)}")
    else:
        print(INVALID_INPUT)


# Run the calculator
calculator()
