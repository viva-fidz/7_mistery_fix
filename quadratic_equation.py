from math import sqrt


def get_roots(a, b, c):
    """calculates roots of discriminan
    
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        root1 = None
        root2 = None
        return root1, root2
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2

