def rotate(text, key):
    final_text = []

    for each_letter in text:
        if not each_letter.isalpha():
            final_text.append(each_letter)
            continue 
        else:
            ascii_value = ord(each_letter)

            if each_letter.islower():
                base = ord('a')
            else:
                base = ord('A')

            alphabet_position = ascii_value - base 
            new_position = (alphabet_position + key) % 26
            final_letter = chr(new_position + base)

            final_text.append(final_letter)
    return "".join(final_text)