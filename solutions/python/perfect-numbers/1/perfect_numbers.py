"""Module for classifying numbers as perfect, abundant, or deficient.

After reading the instructions, it may seem like ancient Greek
mathematicians are about to attack. Fortunately, all we need to do
is add some factors and compare numbers.
"""

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    total = 0
    for each_number in range(1, number):
        if number % each_number == 0:
            total += each_number

    if total == number: 
        return "perfect"
    if total > number:
        return "abundant"
    else:
        return "deficient"
            