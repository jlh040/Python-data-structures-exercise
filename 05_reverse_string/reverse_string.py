def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    list_phrase = list(phrase)
    list_phrase.reverse()
    return ''.join(list_phrase)
