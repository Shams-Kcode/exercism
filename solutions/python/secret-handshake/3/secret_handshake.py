"""Exercism : Secret Handshake"""


def commands(binary_str: str) -> list[str]:
    """Convert a binary string to a list of handshake actions using bitwise masks."""
    
    # 1. Conversion de la chaîne binaire en entier base 10 (ex: "11010" -> 26)
    code = int(binary_str, 2)

    # 2. Table associant chaque masque binaire (puissance de 2) à son action
    actions_map = [
        (1, "wink"),             # 00001
        (2, "double blink"),     # 00010
        (4, "close your eyes"),  # 00100
        (8, "jump"),             # 01000
    ]

    # 3. Test de chaque bit à l'aide de l'opérateur binaire '&'
    handshake = [action for mask, action in actions_map if code & mask]

    # 4. Vérification du 5e bit (valeur 16 = 10000) pour l'inversion
    if code & 16:
        handshake.reverse()

    return handshake