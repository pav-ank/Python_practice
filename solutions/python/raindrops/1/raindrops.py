"""Module for converting numbers into raindrop sounds."""
def convert(number):
    """Convert a number into its corresponding raindrop sounds.

    Parameters:
        number (int): The number to evaluate.

    Returns:
        str: A string containing:
            - "Pling" if the number is divisible by 3,
            - "Plang" if the number is divisible by 5,
            - "Plong" if the number is divisible by 7,
            - a combination of these sounds if multiple factors apply,
            - or the number itself as a string if none of the factors apply.

    """
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    if number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    if number % 3 == 0 and number % 7 == 0:
        return "PlingPlong"
    if number % 5 == 0 and number % 7 == 0:
        return "PlangPlong"
    if number % 3 == 0:
        return "Pling"
    if number % 5 == 0:
        return "Plang"
    return "Plong"
