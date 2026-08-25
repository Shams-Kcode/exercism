""" Exercism : Perfect Numbers"""


def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    
    for i in range(1,number):
        if number % i == 0:
            aliquot_sum += i

    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    return "deficient"