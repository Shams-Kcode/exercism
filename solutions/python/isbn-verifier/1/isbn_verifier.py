"""Exercism : ISBN Verifier"""


def is_valid(isbn):
    """Check if the provided string is a valid ISBN-10"""

    clean_isbn = isbn.replace("-", "")
    total = 0

    if len(clean_isbn) != 10:
        return False
    
    if not clean_isbn[:9].isdigit() or not (clean_isbn[9].isdigit() or clean_isbn[9] == "X"):
        return False

    values = [int(char) if char != "X" else 10 for char in clean_isbn]

    weights = range(10, 0, -1)

    total = sum(digit * weight for digit, weight in zip(values, weights))
    
    return total % 11 == 0