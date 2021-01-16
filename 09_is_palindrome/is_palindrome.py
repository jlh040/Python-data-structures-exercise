def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # remove spaces
    phrase = phrase.replace(' ', '')

    # turn into lowercase
    phrase = phrase.lower()

    # turn into list
    phrase_list = list(phrase)

    # reverse the list
    phrase_list_rv = phrase_list.copy()
    phrase_list_rv.reverse()

    # check if it reads the same forwards and backwards
    return True if phrase_list_rv == phrase_list else False
    
