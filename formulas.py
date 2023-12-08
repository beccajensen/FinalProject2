import sys
import random

def add(values: list) -> float:
    '''
    Sums all floats and integers in values.
    :return: float of the sum of all floats and integers in values
    '''
    return sum(values)

def subtract(values: list) -> float:
    '''
    Does subtraction like: First_element - second_element - third_element - ... - last_element
    '''
    return values[0] - sum(values[1:])

def multiply(values: list) -> float:
    '''
    Multiplies every float in values.
    :return: All non-zero values in values multiplied together.
    '''
    result = 1
    for num in values:
        result *= num
    return result

def divide(values: list) -> float:
    '''
    Divides the first float in values by all other later floats in values
    :return: All values divided from first value in values
    '''
    if any(x == 0 for x in values [1:]):
        raise ZeroDivisionError("Cannot divide by 0")
    elif values[0] == 0:
        return 0
    else:
        result = values[0]
        for num in values[1:]:
            result /= num
        return result
