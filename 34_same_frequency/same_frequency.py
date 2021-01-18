def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # get unique digits
    set1 = set(str(num1))

    # check that the frequencies are the same
    for num in set1:
        if str(num1).count(num) != str(num2).count(num):
            return False
    return True

