def _swap(test_list, x, y):
    """
    Conducts a Pythonic swap within a list between two indicies 

    :param some_list: Python list of integers where the swap will be done 
    :param x: integer of the first index to be swapped with
    :param y: integer of the second index to be swapped with 
    """
    test_list[x], test_list[y] = test_list[y], test_list[x]


def insertion_sort(unsorted, start, end):
    """
    """

    for i in range(1, end + 1):
        j = i

        while (j > 0) and (unsorted[j] < unsorted[j - 1]):
            _swap(unsorted, j, j - 1)
            j -= 1
