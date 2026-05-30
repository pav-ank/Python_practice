"""Function to determine whether a given year is a leap year."""
def leap_year(year):
    """Determine whether a year is a leap year.

    A leap year occurs every 4 years, except for years that are
    divisible by 100 unless they are also divisible by 400.

    Parameters:
        year (int): The year to evaluate.

    Returns:
        bool: True if the year is a leap year, otherwise False.

    Raises:
        ValueError: If the year is less than or equal to zero.
    """
    if year <= 0:
        raise ValueError("Years must be positive")
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
