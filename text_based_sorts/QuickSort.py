from Swap import _swap

def find_pivot(unsorted, start, end): 
    """ 
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
