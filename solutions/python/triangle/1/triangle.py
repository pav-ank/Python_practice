"""Functions to determine the type of triangle based on its side lengths."""

def equilateral(sides):
    """Check if a triangle is equilateral.

    An equilateral triangle has all three sides equal and valid positive lengths.

    Parameters:
        sides (list or tuple): Three side lengths.

    Returns:
        bool: True if all sides are equal and valid, otherwise False.
    """
    a = sides[0]
    b = sides[1]
    c = sides [2]
    if a == 0 or b == 0 or c == 0:
        return False
    if a == b == c:
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
    a = sides[0]
    b = sides[1]
    c = sides [2]
    if a + b >= c:
        if b + c >= a:
            if a + c >= b:
                if a == 0 or b == 0 or c == 0:
                    return False
                if a == b or a == c or b == c:
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
    a = sides[0]
    b = sides[1]
    c = sides [2]
    if a + b >= c:
        if b + c >= a:
            if a + c >= b:
                if a == 0 or b == 0 or c == 0:
                    return False
                if a != b and a != c and b != c:
                    return True
    return False
