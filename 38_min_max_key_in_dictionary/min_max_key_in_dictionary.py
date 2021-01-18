def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    
    # get the key list
    key_list = list(d.keys())

    # sort it
    key_list.sort()

    # get the min and max
    min = key_list[0]
    max = key_list[-1]

    # return a tuple containing the min and max keys
    return (min, max)


