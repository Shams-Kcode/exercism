"""Exercism : Secret Handshake"""

ACTIONS = {
    0 : "jump",
    1 : "close your eyes",
    2 : "double blink",
    3 : "wink"
}


def commands(binary_str):
    """Convert a 5-digit binary string into a sequence of handshake actions."""

    resultat = []
    
    if binary_str[1:] == "0000":
        return resultat
    
    for index, binary in enumerate(binary_str[1:]):
        
        if binary == "0":
            continue
        
        resultat.append(ACTIONS[index])

    if binary_str[0] == "0":
        resultat = resultat[::-1]
        
    return resultat