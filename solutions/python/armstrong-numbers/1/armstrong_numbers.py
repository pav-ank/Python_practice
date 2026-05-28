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
    string_number = str(number)
    armstrong = 0
    power = len(string_number)
    for s in string_number:
        armstrong += int(s) ** power
    if armstrong == number:
        return True
    else:
        return False
    
