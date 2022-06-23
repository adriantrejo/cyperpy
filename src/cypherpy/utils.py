def euclid(a, b):
    """
    "If b is 0, return a, otherwise return the GCD of b and the remainder of a divided by b."
    
    The function is recursive, meaning that it calls itself. The base case is when b is 0, in which case
    the GCD is a. Otherwise, the function calls itself with the arguments b and a % b
    
    :param a: the first number
    :param b: the second number
    :return: The remainder of the division of a by b.
    """
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def modpower(a, n, m):
    """
    Computes a^n mod m in a better way
    
    :param a: the base
    :param n: the number to be factored
    :param m: the modulus
    :return: The remainder of a^n mod m
    """
    r = 1
    y = a % m
    while n > 0:
        if n & 1 == 1:
            r = (r * y) % m
        y = (y * y) % m
        n >>= 1
    return r