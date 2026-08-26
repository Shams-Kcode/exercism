"""Exercism : Resistor Color"""

COLORS = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }


def color_code(color):
    """Determine the number of the color of a transistor"""

    return COLORS[color]

def colors():
    """List the different band colors"""

    return list(COLORS.keys())