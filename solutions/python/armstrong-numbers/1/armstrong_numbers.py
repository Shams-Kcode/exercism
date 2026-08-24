def is_armstrong_number(number):

    str_nb = str(number)
    power = len(str_nb)
    total = sum(int(digit) ** power for digit in str_nb)
    
    return total == number