def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # Make a new list, make a reversed copy of nums
    l1 = []
    nums_copy = nums.copy()
    nums_copy.reverse()

    # Loop through the reversed copy of nums and append each pair of sums to l1
    for i in range(len(nums_copy)-1):
        for j in range(i+1,len(nums_copy)):
            l1.append((nums_copy[i], nums_copy[j], nums_copy[i] + nums_copy[j]))
    
    # filter out any sums that are not equal to goal
    goal_list = [tup for tup in l1 if tup[2] == goal]

    # if there was no pair that summed to goal, return an empty tuple, otherwise return the numbers that summed to goal
    if goal_list == []:
        return ()
    else:
        return (goal_list[-1][1], goal_list[-1][0])

