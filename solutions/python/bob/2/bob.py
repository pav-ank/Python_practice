"""
Bob is a teenager with a very low-effort communication style.
He tends to respond only when necessary and prefers minimal engagement.
"""
def response(hey_bob):
    """Generate Bob's response based on the input message.

    Bob responds differently depending on whether the input is:
    - a question
    - shouted (all uppercase letters)
    - a shouted question
    - silence (empty or whitespace only)
    - or anything else

    Parameters:
        hey_bob (str): The input message to respond to.

    Returns:
        str: Bob's response according to conversational rules.
    """
    hey_bob_1 = hey_bob.strip()
    if hey_bob_1.isupper() and "?" in hey_bob_1:
        return "Calm down, I know what I'm doing!" 
    if not hey_bob_1:
        return "Fine. Be that way!"
    if  hey_bob_1[-1] == "?":
        return "Sure."
    if hey_bob_1.isupper():
        return "Whoa, chill out!"
    return "Whatever."
