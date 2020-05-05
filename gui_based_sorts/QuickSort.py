import time 
from Swap import _swap

def find_pivot(data_list, start, end): 
    first = data_list[start]
    middle = data_list[(start + end) // 2] 
    last = data_list[end] 

    if (middle <= first <= last) or (last <= first <= middle): 
        return first 
    elif (first <= middle <= last) or (last <= middle <= first): 
        return middle 
    elif (first <= last <= middle) or (middle <= last <= first): 
        return last 

def partition(): 
    pass

def quick_sort(data_list, start, end, draw_data, time_value): 
    if start >= end: 
        return 

    pivot_index = partition(data_list, start, end, draw_data, time_value) 

    # sorting the first half of the data 
    quick_sort(data_list, start, pivot_index, draw_data, time_value) 

    # sorting the second half of the data 
    quick_sort(data_list, pivot_index + 1, end, draw_data, time_value)
