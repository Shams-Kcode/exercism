"""Exercism: Flatten Array"""


def flatten(iterable):
    """Take a nested array of any depth and return a fully flattened array,
    excluding any None values.
    """

    result = []

    for item in iterable:

        if isinstance(item, list):
            result.extend(flatten(item))
    
        elif item is not None:
            result.append(item)

    return result