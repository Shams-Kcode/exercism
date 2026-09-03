"""Exercism: Difference of Squares"""


def square_of_sum(number):

    result_square_of_sum = 0

    while number != 0:
        result_square_of_sum += number
        number -= 1
    
    return result_square_of_sum ** 2


def sum_of_squares(number):

    result_sum_of_squares = 0

    while number != 0:
        result_sum_of_squares += number ** 2
        number -= 1
    
    return result_sum_of_squares


def difference_of_squares(number):

    return square_of_sum(number) - sum_of_squares(number)
