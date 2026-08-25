"""Module providing a function to convert a number into raindrop sounds."""


def convert(number: int) -> str:
    """Convert a number into raindrop sounds based on its factors.

    Parameters:
        number (int): The number to evaluate.

    Returns:
        str: The concatenated raindrop sounds, or the number as a string.
    """

    sound = ""

    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"

    if not sound:
        return str(number)

    return sound if sound else str(number)