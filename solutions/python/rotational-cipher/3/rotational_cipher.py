"""Implements a rotational (Caesar) cipher for encoding text using a shift key."""
def rotate(text, key):
    """
    Encode a given text using a Caesar cipher with the specified rotation key.

    Each alphabetical character in the input text is shifted forward by
    'key' positions in the alphabet. The shift wraps around after 'z' or 'Z'.
    Non-alphabetical characters (spaces, punctuation, numbers) are preserved
    without modification.

    Args:
        text (str): The input string to be encoded.
        key (int): The number of positions to rotate each letter.

    Returns:
        str: The encoded string after applying the rotational cipher.
    """
    final_text = []

    for each_letter in text:
        if not each_letter.isalpha():
            final_text.append(each_letter)
            continue 
        ascii_value = ord(each_letter)

        if each_letter.islower():
            base = ord("a")
        else:
            base = ord("A")

        alphabet_position = ascii_value - base 
        new_position = (alphabet_position + key) % 26
        final_letter = chr(new_position + base)

        final_text.append(final_letter)
    return "".join(final_text)