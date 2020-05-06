import time 

def merge(data_list, start, middle, end, draw_data, time_value): 
    # update color here 

    start_list = data_list[start:middle + 1] 
    end_list = data_list[middle + 1:right + 1 ]

    left_index = 0 
    right_index = 0 

    for i in range(left, right + 1): 
        if left_index < len(start_list) and right_index < len(end_list): 
            if start_list[left_index] <= end_list[right_index]: 
                data_list[i] = start_list[left_index]
                left_index += 1 
            else: 
                data_list[i] = end_list[right_index] 
        
        elif left_index < len(start_list): 
            data_list[i] = start_list[left_index]
            left_index += 1 
        else: 
            data_list[i] = end_list[right_index]
            right_index += 1 

    # update colors here too 
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
