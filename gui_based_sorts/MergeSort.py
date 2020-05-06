import time 

def merge(data, start, end, draw_data, time_value): 

    pass

def merge_sort(data_list, start, end, draw_data, time_value): 
    if start > end: 
        return 

    middle_index = (start + end) // 2 

    # sort the first half of the data 
    merge_sort(data_list, start, middle_index, draw_data, time_value) 

    # sort the second half of the data 
    merge_sort(data_list, middle_index + 1, end, draw_data, time_value) 
    
    merge(data_list, start, middle_index, end, draw_data, time_value)
