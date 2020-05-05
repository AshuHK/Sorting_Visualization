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

def partition(data_list, start, end, draw_data, time_value):
    pivot_value = find_pivot(data_list, start, end) 

    i = start - 1 

    for j in range(start, end + 1): 
        if data_list[j] < pivot_value: 
            i += 1 
            _swap(data_list, i, j) 
            
            color_list = ["red" for x in range(len(data_list))]

            for x in range(len(color_list)): 
                if (x == i) or (x == j):
                    color_list[x] = "green"
            
            draw_data(data_list, color_list)
            time.sleep(time_value)
    
    i += 1 
    swap_index = data_list.index(pivot_value)
    _swap(data_list, i, swap_index)

    color_list = ["red" for x in range(len(data_list))] 

    for x in range(len(color_list)): 
        if (x == i) or (x == swap_index): 
            color_list[x] = "green" 
    
    draw_data(data_list,color_list)
    time.sleep(time_value)

    return i 

def quick_sort(data_list, start, end, draw_data, time_value): 
    if start >= end: 
        return 

    pivot_index = partition(data_list, start, end, draw_data, time_value) 

    # sorting the first half of the data 
    quick_sort(data_list, start, pivot_index, draw_data, time_value) 

    # sorting the second half of the data 
    quick_sort(data_list, pivot_index + 1, end, draw_data, time_value)

    draw_data(data_list, ["green" for i in range(len(data_list))])
