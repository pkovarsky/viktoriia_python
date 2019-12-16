"""- Implement to boolean function. Retrieve different type of object returns
True or False"""


def is_empty(cart_items_added, cart_items):
    """
The function checks if the cart is empty.
    :param cart_items_added: list of recently added items
    :param cart_items: list of existed cart items
    :return: bool
    """
    if len(cart_items_added) == 0 and len(cart_items) == 0:
        result = True
    else:
        result = False

    return result


print(is_empty(cart_items_added=["headphones"],
               cart_items=[]))


def is_student(student):
    """
The function checks if the person is a listed student.
    :param student: name of the person
    :return: bool
    """
    students = ["Steve", "Matt", "Ellie", "Dan", "Mark", "Angela"]
    if student in students:
        result = True
    else:
        result = False

    return result


print(is_student("Anthony"))


# - Implement 2 functions for calculation Factorial number (Method retrieves
# number, returns it Factorial).
# First function uses while loop for calculation
# Second function uses for loop for calculation
# For avoid stack overflow do not calculate Factorial number more than 100500.
# Use default function argument for limit.
# Negative, fractional, not a number argument forbidden.


def to_factorial_while(number):
    """
This function accepts any int type and calculates factorial for this input
using while loop. Other types of input are neglected.
    :param number: input value to calculate factorial for it
    :return: int
    """
    if type(number) == int:
        factorial = " "
        if 1 <= number <= 9:
            factorial = 1
            i = 1
            while i <= number + 1:
                factorial = factorial * i
                i += 1
        elif number == 0:
            factorial = 1
        else:
            print("Forbidden input. Insert number from 1 to 9.")

        return factorial

    print("Forbidden input. Insert an integer.")
    return None


print(to_factorial_while(2/3))


def to_factorial_for(number):
    """
This function accepts string type, detects if there are int number and
calculates factorial for this input using for loop. Other types of input are
neglected.
    :param number: input number to calculate factorial for it
    :return: int
    """
    if number.isdigit():
        number = int(number)
        factorial = " "
        if 1 <= number <= 9:
            factorial = 1
            for i in range(1, number + 1):
                factorial = factorial * i
        elif number == 0:
            factorial = 1
        else:
            print("Forbidden input. Insert number from 1 to 9.")

        return factorial

    print("Forbidden input. Insert an integer.")
    return None


print(to_factorial_for("1.1"))


# - Implement function to convert cm to inches and vice versa
# (convertCmToInches).


def convert_cm_to_inch(length):
    """
This function makes cm to inch conversion.
    :param length: input length in centimeters
    :return: float
    """
    if type(length) == float or type(length) == int:
        result = length / 2.54

        return result

    print("Please, insert a number")
    return None


print(convert_cm_to_inch(12))


def convert_inch_to_cm(length):
    """
This function makes inch to cm conversion.
    :param length: input length in inches
    :return: float
    """
    if type(length) == float or type(length) == int:
        result = length * 2.54

        return result

    print("Please, insert a number")

    return None


print(convert_inch_to_cm("yu"))

# - Implement printDiagonal function which wrap convertCmToInches function
# and print result. (call convertCmToInches and print result of evaluation).


def print_diagonal(length):
    """
The function prints out the diagonal calculated based on inserted value in cm.
    :param length: input length to be converted
    :return: float
    """
    converted = convert_cm_to_inch(length)

    return converted


print(f"Diagonal is: {print_diagonal(12)}")


# - Implement processArgs function which retrieves callback as a first
# argument, remaining args has various length.
# Default value for callback is a standard print function.
# Call this function with printDiagonal function and remaining args as cm or
# inches.
# -processArgs(printDiagonal, 50, True)
# -processArgs(print, 'test')
# -processArgs(len, [])

# TBD
