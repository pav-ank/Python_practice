'''
First, raise a ValueError if the number of squares is less than 1 or greater than 64, since a chessboard only has 64 squares.

Next, initialize the current value to 1. Then iterate through the squares, doubling the value at each step to represent the number of grains on the current square.

For the total function, initialize a total counter at 0. Then loop through all 64 squares, use the square function to compute the grains on each square, and accumulate the results into total.
'''

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    current_squared = 1
    for squared_number in range(1, number): #The variable squared_number is only used for repetition                                               and is not needed for any further logic.
        current_squared = current_squared * 2
      
    return current_squared


def total():
    grand_total = 0
    for i in range(1, 65):
        grand_total += square(i)
    return grand_total
