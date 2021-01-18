def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # get the TL-to-BR diagonal sum
    count1 = 0
    for i in range(len(matrix)):
        count1 += matrix[i][i]
    
    # get the TR-to-BL diagonal sum
    count2 = 0
    row = 0
    for i in range(len(matrix) - 1, -1, -1):
        count2 += matrix[row][i]
        row += 1
    
    # return the sum of the diagonals
    return count1 + count2
