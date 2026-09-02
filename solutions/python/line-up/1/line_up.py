"""Exercism: Line Up"""


def line_up(name, number):
    """Generate a polite ticket message for a customer using the correct ordinal numeral."""

    str_num = str(number)

    if len(str_num) >= 2 and str_num[-2:] in ("11", "12", "13"):
        suffix = "th"
    else:
        last_digit = str_num[-1]
        
        if last_digit == "1":
            suffix = "st"
        elif last_digit == "2":
            suffix = "nd"
        elif last_digit == "3":
            suffix = "rd"
        else:
            suffix = "th"
    
    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"