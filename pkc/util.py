"""
    Created by mbenlioglu on 11/22/2017
"""


def multiplicative_inverse(num, modulo):
    """
    Return the multiplicative inverse of the given number in given modulo or raises a ValueError if no inverse exists.
    :param num: Number to be inverted
    :type num: int
    :param modulo:
    :type modulo: int
    :raises ValueError if num has no inverse
    :return: multiplicative inverse of the number in the given modulo
    """
    t = 0
    r = modulo
    newt = 1
    newr = num

    while newr != 0:
        quotient = r / newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError('number does not have a multiplicative inverse in given modulo')
    return t if t > 0 else t + modulo


def gcd(num1, num2):
    """
    Calculates the greatest common divisor of given 2 numbers
    :param num1: First number
    :type num1: int
    :param num2: Second number
    :type num2
    :return: Greatest common divisor
    """
    big, small = (num1, num2) if num1 > num2 else (num2, num1)

    remainder = -1
    while remainder != 0:
        quotient = big / small
        remainder = big - quotient * small
        big, small = small, remainder
    return big
