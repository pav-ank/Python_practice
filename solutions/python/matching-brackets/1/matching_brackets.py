"""Checks whether all brackets in a string are properly balanced and nested."""
def is_paired(input_string):
    """
    Determine if a string has properly balanced brackets.

    The function checks whether every opening bracket has a corresponding
    closing bracket in the correct order. It supports three types of brackets:
    (), [], and {}. All other characters are ignored.

    Args:
        input_string (str): The string containing brackets and other characters.

    Returns:
        bool: True if all brackets are balanced and correctly nested,
              False otherwise.
    """
    brackets = []
    pairs = {
        ']' : '[',
        ')' : '(',
        '}' : '{'
    }
    
        
    for text in input_string:
        if text in '[({':
            brackets.append(text)
        
        elif text in'])}':
            if not brackets:
                return False

            if brackets[-1] == pairs[text]:
                brackets.pop()
            else:
                return False
                
    
    return len(brackets) == 0
            
       
            