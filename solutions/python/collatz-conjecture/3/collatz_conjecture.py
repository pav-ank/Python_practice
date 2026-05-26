"""
Collatz Conjecture implementation.

This module provides a function to compute the number of steps required
to reduce a given positive integer to 1 using the Collatz sequence rules:

- If the number is even, divide it by 2.
- If the number is odd, multiply it by 3 and add 1.

The process repeats until the number becomes 1, and the function
returns the total number of steps taken.

Raises:
    ValueError: If the input number is not a positive integer.
"""
def steps(number):

    """
    First, initialize total to 0 and raise a ValueError if the input number is less than or equal to      0.
    This is important because the Collatz sequence is undefined for non-positive integers and would       otherwise result in an infinite loop.
    
    Next, use a while loop that continues until the number becomes 1.
    
    Inside the loop:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    After each operation, increment the total step counter.
    
    This continues until the sequence reaches 1.
    """
    total = 0
    if number < 0 or number == 0: 
        raise ValueError("Only positive integers are allowed")
        
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            total += 1
        else: 
            number = (number * 3) + 1
            total += 1
        
    return total
