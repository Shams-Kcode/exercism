"""Exercism : Pangram"""


def is_pangram(sentence):
    """Determine if the sentence is a pangram or not"""

    return set("abcdefghijklmnopqrstuvwxyz") <= set(sentence.lower())