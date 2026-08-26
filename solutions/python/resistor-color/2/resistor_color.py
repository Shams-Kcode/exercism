"""Exercism : Resistor Color"""

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


def color_code(color: str) -> int:
    """Return the numerical value associated with a specific resistor color band."""

    return COLORS_LIST.index(color)


def colors() -> list[str]:
    """Return the complete list of all resistor band colors ordered by value."""

    return COLORS_LIST.copy()