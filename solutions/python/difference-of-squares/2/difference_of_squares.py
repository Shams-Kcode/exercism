"""Exercism: Difference of Squares"""


def square_of_sum(number):
    """Calculate the square of the sum of the first n natural numbers."""

    return (number * (number + 1) // 2) ** 2


def sum_of_squares(number):
    """Calculate the sum of the squares of the first n natural numbers."""

    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number):

    return square_of_sum(number) - sum_of_squares(number)
