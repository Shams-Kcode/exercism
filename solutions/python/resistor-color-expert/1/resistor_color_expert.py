"""Exercism : Resistor Color Expert"""

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

TOLERANCE = {
    "grey" : 0.05,
    "violet" : 0.1,
    "blue" : 0.25,
    "green" : 0.5,
    "brown" : 1,
    "red" : 2,
    "gold" : 5,
    "silver" : 10
}


def resistor_label(colors):
    """Calculate the resistance value and tolerance from 1, 4, or 5 color bands."""

    if len(colors) == 1:
        return "0 ohms"

    digit_bands = colors[:-2]
    multiplier_band = colors[-2]
    tolerance_band = colors[-1]

    digits = 0
    for band in digit_bands:
        digits = (digits * 10) + COLORS_LIST.index(band)

    exponent = COLORS_LIST.index(multiplier_band)
    total_ohms = digits * (10**exponent)
    
    for threshold, unit in PREFIXES:
        if total_ohms >= threshold:
            scaled_value = total_ohms / threshold

            # Si le nombre est un entier exact (ex: 33.0), on le formate en entier (33)
            if scaled_value.is_integer():
                scaled_value = int(scaled_value)

            tolerance_value = TOLERANCE[tolerance_band]
            return f"{scaled_value} {unit} ±{tolerance_value}%"

    return "0 ohms"
        