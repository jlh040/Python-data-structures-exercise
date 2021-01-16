def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    # turn lists into sets
    set_l1 = set(l1)
    set_l2 = set(l2)

    # get the intersection
    intersection_of_lists = set_l1 & set_l2

    #turn back into a list and return
    return list(intersection_of_lists)
