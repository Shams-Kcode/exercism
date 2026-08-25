"""Exercism : Reverse String"""


def reverse(text):
    """Reverse a given string."""

    reversed_text = ""

    return reversed_text.join(letter for letter in reversed(text))