def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # get uppercase and lowercase of to_swap:
    to_swap_both = [to_swap.upper(), to_swap.lower()]

    # turn phrase into list
    phrase_list = list(phrase)

    # iterate and swap casing
    for idx in range(len(phrase_list)):
        if phrase_list[idx] in to_swap_both and phrase_list[idx].isupper():
            phrase_list[idx] = phrase_list[idx].lower()
        elif phrase_list[idx] in to_swap_both and phrase_list[idx].islower():
            phrase_list[idx] = phrase_list[idx].upper()
    
    # return a concatenated version of the list
    return ''.join(phrase_list)
        
