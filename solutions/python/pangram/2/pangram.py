"""Exercism : Pangram"""

import string


ALPHABET = set(string.ascii_lowercase)


def is_pangram(sentence):
    """Determine if the sentence is a pangram or not"""

    return ALPHABET <= set(sentence.lower())