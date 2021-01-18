def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # split the string up
    split_phrase = phrase.split(' ')

    # make each word lowercase
    split_phrase = [word.lower() for word in split_phrase]

    # capitalize each word
    split_phrase = [word.capitalize() for word in split_phrase]

    # turn into a string again
    return ' '.join(split_phrase)
    
