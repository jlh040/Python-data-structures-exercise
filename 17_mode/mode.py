def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # make a dictionary of frequencies
    freq_dict = {number: nums.count(number) for number in nums}

    # set a default mode and the number of times it occurs
    largest = freq_dict[list(freq_dict.keys())[0]]
    mode_of_list = list(freq_dict.keys())[0]

    # if one of the frequences is larger then the current largest frequency
    # set the mode to the corresponding number
    for k in freq_dict.keys():
        if freq_dict[k] > largest:
            mode_of_list = k
            largest = freq_dict[k]
    
    # return the mode
    return mode_of_list
    