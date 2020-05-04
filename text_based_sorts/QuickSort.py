from Swap import _swap


def find_pivot(unsorted, start, end):
    """
    Find the pivot value using the Median of Three method in a Python list
    Expected Complexity: O(1) (time and space)

    :param unsorted: an unsorted Python list to find the pivot value in
    :param start: integer of starting index to find the pivot value in
    :param end: integer of ending index to find the pivot value in

    :return: the value of the pivot found using the Median of Three method
    """
    first = unsorted[start]
    middle = unsorted[(start + end) // 2]
    last = unsorted[end]

    if (middle <= first <= last) or (last <= first <= middle):
        return first
    elif (first <= middle <= last) or (last <= middle <= first):
        return middle
    elif (first <= last <= middle) or (middle <= last <= first):
        return last


def partition(unsorted, start, end):
    """
    Will partition a list given a certain range for values greater and 
    less than the pivot to be a certain side 
    Expected complexity: O(n) (time) and O(1) (space) 

    :param unsorted: an unsorted Python list to be partitioned 
    :param start: integer of starting index within the list 
    :param end: integer of ending index within the list 

    :return: index of where hte pivot value ends in the list 
    """
    pivot_value = find_pivot(unsorted, start, end) 

    i = start - 1 
    for j in range(start, end + 1): 
        if unsorted[j] < pivot_value: 
            i += 1 
            _swap(unsorted, i, j) 
    
    _swap(unsorted, i + 1, unsorted.index(pivot_value)) 

    i += 1 
    return i 


def quick_sort(unsorted, start, end):
    """
    """
    pass
