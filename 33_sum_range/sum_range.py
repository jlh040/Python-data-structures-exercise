def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    count = 0
    if end:
        if end <= len(nums) - 1:
            for idx in range(start, end + 1):
                count += nums[idx]
            return count
        elif end > len(nums) - 1:
            for idx in range(start, len(nums)):
                count += nums[idx]
            return count
    else:
        for idx in range(start,len(nums)):
            count += nums[idx]
        return count

