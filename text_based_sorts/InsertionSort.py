def _swap(test_list, x, y):
    """
    Conducts a Pythonic swap within a list between two indicies 
    Expected Complexity: O(1) (time and space) 

    :param some_list: Python list of integers where the swap will be done 
    :param x: integer of the first index to be swapped with
    :param y: integer of the second index to be swapped with 
    """
    test_list[x], test_list[y] = test_list[y], test_list[x]


def insertion_sort(unsorted, start, end):
    """
    Does an insertion sort on a Python list given a range of indicies
    Expected Complexity: O(n^2) (time) and O(1) (space) 

    :param unsorted: unsorted Python list to be sorted 
    :param start: integer of the starting index to be sorted  
    :param end: integer of the ending index to be sorted  
    """

    for i in range(1, end + 1):
        j = i

        while (j > 0) and (unsorted[j] < unsorted[j - 1]):
            _swap(unsorted, j, j - 1)
            j -= 1
