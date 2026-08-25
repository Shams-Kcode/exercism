"""Module providing a function to determine the number of steps of the Collatz"""

def steps(number : int) -> int :
    """Determine the number of steps of the Collatz Conjecture.

    Parameters:
        number (int): The number to check (must be strictly positive).

    Returns:
        int: The number of steps to reach 1.

    Raises:
        ValueError: If number is not a strictly positive integer.
    """
    
    steps_counter = 0
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if number % 2 == 0:
            number //= 2
        
        else:
            number = 3 * number + 1
        
        steps_counter += 1
            
    return steps_counter
    
