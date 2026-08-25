""" Exercism : Darts """

import math


def score(x: float, y: float) -> int:
    """Calculate the score of a single dart toss given its coordinates (x, y).
    
    distance = math.hypot(x, y)

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1

    return 0
    """

    distance = math.hypot(x, y)
    
    scores = {
        1 : 10,
        5 : 5,
        10 : 1
    }
    
    return next(
        (points for radius, points in scores.items() if distance <= radius),
        0,
    )