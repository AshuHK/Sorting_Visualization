def _swap(test_list, x, y):
    """
    Conducts a Pythonic swap within a list between two indicies 
    Expected Complexity: O(1) (time and space) 

    :param some_list: Python list of integers where the swap will be done 
    :param x: integer of the first index to be swapped with
    :param y: integer of the second index to be swapped with 
    """
    test_list[x], test_list[y] = test_list[y], test_list[x]


def selection_sort(unsorted): 
    """
    Does an selection sort on a Python list 
    Expected Complexity: O(n^2) (time) and O(1) (space)

    :param unsorted: unsorted Python list to be sorted  
    """
    for i in range(len(unsorted)): 

        min_index = i 
        for j in range(i + 1, len(unsorted)): 
            if unsorted[min_index] > unsorted[j]: 
                min_index = j 

        _swap(unsorted, i, min_index)
