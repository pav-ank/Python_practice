"""Module for translating words into Pig Latin.

Many brain cells were sacrificed in the making of this solution.
"""
def translate(text):
    """Translate a word or sentence into Pig Latin.

    Parameters:
        text (str): The word or sentence to translate.

    Returns:
        str: The translated Pig Latin text.

    Note:
        - Words beginning with a vowel sound receive 'ay' at the end.
        - Words beginning with consonant sounds move the consonant cluster
          to the end before adding 'ay'.
        - Special cases such as 'qu', 'xr', 'yt', and 'y' are handled
          according to Pig Latin rules.
        - Multiple words are translated individually and then joined
          back into a sentence.
    """
    words = text.split()
    translated_words = []
    for word in words:
        vowel = ('a', 'e', 'i', 'o', 'u')
        other = 'qu'
        conso = 0
    #rule 1
        if word.startswith(vowel) or word.startswith(('xr', 'yt', 'ay')):
            translated_words.append(word + 'ay')
            continue
        
        while conso < len(word) and  word[conso] not in vowel:
            if word[conso] == 'y' and conso > 0:
                break
            if word.startswith(other, conso):
                conso += 2
                break
            conso += 1
    
        rule3_text = word[conso:] + word[:conso] + 'ay'
        translated_words.append(rule3_text)
    return ' '.join(translated_words)


    
        
    
