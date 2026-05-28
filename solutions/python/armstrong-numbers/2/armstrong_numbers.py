'''
Checks whether a number is an Armstrong number.

An Armstrong number is a number that is equal to the sum
of its digits, where each digit is raised to the power
of the total number of digits in the number.

Args:
    number (int): The number to check.

Returns:
    bool: True if the number is an Armstrong number,
    otherwise False.
'''

def is_armstrong_number(number):
    """
    Convert the number into a string to separate its digits.
    
    Initialize a sum variable to store the Armstrong calculation.
    The power is determined by the total number of digits in the number.
    
    Loop through each digit, convert it back to an integer,
    raise it to the calculated power, and add it to the sum.
    
    Finally, return True if the computed value equals the original number,
    otherwise return False.
    """
    string_number = str(number)
    armstrong = 0
    power = len(string_number)
    for character in string_number:
        armstrong += int(character) ** power
    if armstrong == number:
        return True

    return False
    
