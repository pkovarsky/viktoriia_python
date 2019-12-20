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
        return True

    return False


print(is_empty(cart_items_added=[],
               cart_items=[]))

STUDENTS = ["Steve", "Matt", "Ellie", "Dan", "Mark", "Angela"]


def is_student(student):
    """
    The function checks if the person is a listed student.
    :param student: name of the person
    :return: bool
    """
    if student in STUDENTS:
        return True

    return False


print(is_student("Steve"))


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
    if isinstance(number, int):
        factorial = 1
        if 1 <= number <= 9:
            i = 1
            while i <= number:
                factorial = factorial * i
                i += 1
        elif number == 0:
            return 1
        else:
            print("Forbidden input. Insert number from 1 to 9.")
            return None

        return factorial

    print("Forbidden input. Insert an integer.")
    return None


print(to_factorial_while(3))


def to_factorial_for(number):
    """
    This function accepts string type, detects if there are int number and
    calculates factorial for this input using for loop. Other types of input
    are neglected.
    :param number: input number to calculate factorial for it
    :return: int
    """
    if isinstance(number, int):
        number = int(number)
        factorial = 1
        if 1 <= number <= 9:
            for i in range(1, number + 1):
                factorial = factorial * i
        elif number == 0:
            return 1
        else:
            print("Forbidden input. Insert number from 1 to 9.")
            return None

        return factorial

    print("Forbidden input. Insert an integer.")
    return None


print(to_factorial_for(9))


# - Implement function to convert cm to inches and vice versa
# (convertCmToInches).


def convert_to(length, uom):
    """
    This function makes cm to inch conversion.
    :param length: input length in centimeters
    :return: float
    """
    if isinstance(length, (float, int)):
        if uom == "to cm":
            converted = length * 2.54
            return converted
        elif uom == "to inch":
            converted = length / 2.54
            return converted
        print("Select 'to cm' or 'to inch' to complete conversion")
        return None

    print("Please, insert a number")
    return None


print(convert_to(10, "to cm"))


# - Implement printDiagonal function which wrap convertCmToInches function
# and print result. (call convertCmToInches and print result of evaluation).


def print_diagonal(length, uom):
    """
    The function prints out the diagonal calculated based on inserted values.
    :param length: input length to be converted
    :param uom: what uom to convert to (cm, inch)
    """
    print(convert_to(length, uom))


print_diagonal(5.08, "to inch")


# - Implement processArgs function which retrieves callback as a first
# argument, remaining args has various length.
# Default value for callback is a standard print function.
# Call this function with printDiagonal function and remaining args as cm or
# inches.
# -processArgs(printDiagonal, 50, True)
# -processArgs(print, 'test')
# -processArgs(len, [])

def process_args(callback, *args):
    """
    Function that processes any input arguments with the function given as
    the first argument
    :param callback: default print()
    :param args: any value(s) that satisfy callback function criteria
    """
    callback(*args)


print(process_args(print, "test"))
