"""
identifying whether a given word or phrase qualifies as an isogram.
"""
def is_isogram(string):
    """
    Check if a string is an isogram.
    
    An isogram is a word or phrase without any repeating letters. 
    This function is case-insensitive and ignores non-alphabetic 
    characters such as spaces, hyphens, and punctuation. An empty 
    string is considered a valid isogram.

    Parameters:
    string (str): The text phrase or word to evaluate.

    Returns:
    bool: True if the string is an isogram, False otherwise.
    """
    letters = []
    for char in string:
        if char.isalpha():
            letters.append(char.lower())

    if len(letters) == len(set(letters)):
        return True
    return False
