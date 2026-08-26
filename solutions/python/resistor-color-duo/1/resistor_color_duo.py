"""Exercism : Resistor Color Duo"""

COLORS_LIST = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    """Return the value of 2 transistors"""

    return COLORS_LIST.index(colors[0]) * 10 + COLORS_LIST.index(colors[1])