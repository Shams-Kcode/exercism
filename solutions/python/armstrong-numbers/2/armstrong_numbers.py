"""Module providing a function to determine if a number is an Armstrong number"""

def is_armstrong_number(number):
    """Determine if a number is an Armstrong number.

    Parameters:
        number (int): The number to check.
    Returns:
        bool: True if `number` is an Armstrong number, False otherwise.
    """

    str_nb = str(number)
    power = len(str_nb)
    total = sum(int(digit) ** power for digit in str_nb)
    
    return total == number