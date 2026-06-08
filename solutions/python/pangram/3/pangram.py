"""Module for checking whether a sentence is a pangram.

A pangram is a sentence that contains every letter of the alphabet
at least once.
"""

def is_pangram(sentence):
    """Determine whether a sentence is a pangram.
    
    Parameters:
        sentence (str): The sentence to evaluate.
    
    Returns:
        bool: True if the sentence contains every letter from
        'a' to 'z' at least once, otherwise False.
    
    Note:
        - Uppercase and lowercase letters are treated the same.
        - Non-alphabetic characters are ignored.
        - An empty sentence is not a pangram.
    """
    alphabets_string = "abcdefghijklmnopqrstuvwxyz"
    lowercase_sentence = sentence.lower()
    if not sentence:
        return False
    
    return all(letter in lowercase_sentence for letter in alphabets_string)
