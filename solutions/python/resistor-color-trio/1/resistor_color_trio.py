"""Exercism : Resistor Color Trio"""


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

PREFIXES = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
    (1, "ohms"),
]


def label(colors: list[str]) -> str:
    """Calculate the resistance value from three color bands and format it with metric prefixes."""

    digits = (COLORS_LIST.index(colors[0]) * 10) + COLORS_LIST.index(colors[1])
    exponent = COLORS_LIST.index(colors[2])
    total_ohms = digits * (10**exponent)

    for threshold, unit in PREFIXES:
        if total_ohms >= threshold:
            scaled_value = total_ohms // threshold
            return f"{scaled_value} {unit}"

    return f"{total_ohms} ohms"