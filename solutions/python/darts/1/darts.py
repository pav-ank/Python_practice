""" Calculates the points earned for a single dart throw based on its coordinates.
"""

def score(x, y):
    """Calculates the points earned for a single dart throw.

    Args:
        x: A float or int representing the x-coordinate of the dart.
        y: A float or int representing the y-coordinate of the dart.

    Returns:
        An integer score (10, 5, 1, or 0) based on the dart's distance 
        from the center target (0, 0).
    """
    distance = (x**2 + y**2)**0.5
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
