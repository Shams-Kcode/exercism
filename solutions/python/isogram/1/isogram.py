"""Exercism : Isogram"""


def is_isogram(phrase):
    """Determine if a word or phrase is an isogram."""

    letters = [char.lower() for char in phrase if char.isalpha()]

    return len(letters) == len(set(letters))
