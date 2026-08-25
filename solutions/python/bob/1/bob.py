"""Module providing a function to simulate Bob's teenage responses."""


def response(hey_bob: str) -> str:
    """Predict Bob's response based on the phrasing and tone.

    Parameters:
        hey_bob (str): The sentence addressed to Bob.

    Returns:
        str: Bob's concise response.
    """
    
    cleaned_input = hey_bob.strip()

    if not cleaned_input:
        return "Fine. Be that way!"

    is_question = cleaned_input.endswith("?")
    is_yelling = cleaned_input.isupper()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    if is_yelling:
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."