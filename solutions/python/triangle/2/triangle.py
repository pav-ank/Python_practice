"""Functions to determine the type of triangle based on its side lengths."""

def equilateral(sides):
    """Check if a triangle is equilateral.

    An equilateral triangle has all three sides equal and valid positive lengths.

    Parameters:
        sides (list or tuple): Three side lengths.

    Returns:
        bool: True if all sides are equal and valid, otherwise False.
    """
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides [2]
    if side_1 == 0 or side_2== 0 or side_3 == 0:
        return False
    if side_1 == side_2 == side_3:
        return True
    return False


def isosceles(sides):
    """Check if a triangle is isosceles.

    An isosceles triangle has at least two equal sides and satisfies triangle inequality rules.

    Parameters:
        sides (list or tuple): Three side lengths.

    Returns:
        bool: True if the triangle is isosceles, otherwise False.
    """
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides [2]
    if side_1 + side_2 >= side_3:
        if side_2 + side_3 >= side_1:
            if side_1 + side_3 >= side_2:
                if side_1 == 0 or side_2 == 0 or side_3 == 0:
                    return False
                if side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
                    return True
    return False

def scalene(sides):
    """Check if a triangle is scalene.

    A scalene triangle has all sides of different lengths and satisfies triangle inequality rules.

    Parameters:
        sides (list or tuple): Three side lengths.

    Returns:
        bool: True if the triangle is scalene, otherwise False.
    """
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides [2]
    if side_1 + side_2 >= side_3:
        if side_2 + side_3 >= side_1:
            if side_1 + side_3 >= side_2:
                if side_1 == 0 or side_2 == 0 or side_3 == 0:
                    return False
                if side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
                    return True
    return False
