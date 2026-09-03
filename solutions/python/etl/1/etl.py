"""Exercism : ETL"""


def transform(legacy_data):
    """Transform legacy letter scoring using a dictionary comprehension."""
    
    return {
        letter.lower(): score
        for score, item in legacy_data.items()
        for letter in item
    }