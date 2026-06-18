"""Validate whether a given string is a valid ISBN-10 number."""
def is_valid(isbn):
    """
    Validates whether a given string is a valid ISBN-10 number.

    An ISBN-10 is valid if:
    - It contains exactly 10 characters (after removing hyphens)
    - The first 9 characters are digits
    - The last character is either a digit or 'X' (representing 10)
    - The weighted sum of all digits (from 10 to 1) is divisible by 11

    Hyphens are ignored during validation.

    Args:
        isbn (str): The ISBN-10 string to validate.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """
    clean_isbn = isbn.replace("-", "")
    number = 10
    total = 0
    if len(clean_isbn) != 10:
        return False
        
    if not clean_isbn[0:-1].isdigit():
        return False
        
    if not(clean_isbn[-1].isdigit() or clean_isbn[-1] == "X"):
        return False
    
    
    for each_char in clean_isbn:
        if number < 1:
            break
        if each_char == "X":
            value = 10
        else:
            value = int(each_char)
        total += value * number
        number -= 1

    if total % 11 == 0:
        return True
    return False