from Swap import _swap

def find_pivot(unsorted, start, end): 
    """ 
    Find the pivot value using the Median of Three method in a Python list 
    Expected Complexity: O(1) (time and space) 

    :param unsorted: an unsorted Python list to find the pivot value in 
    :param start: starting index to find the pivot value in 
    :param end: ending index to find the pivot value in 

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

def quick_sort(unsorted, start, end): 
    pass
