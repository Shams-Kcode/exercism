"""Exercism : Rotational Cipher"""

import string


def rotate(text, key):
    """Transpose the letter in text using an integer key"""

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    shift = key % 26

    shifted_lower = lower[shift:] + lower[:shift]
    shifted_upper = upper[shift:] + upper[:shift]

    translation_table = str.maketrans(
        lower + upper,
        shifted_lower + shifted_upper,
    )

    return text.translate(translation_table)