import time 
from Swap import _swap

def heapify(data_list, size, root_index, draw_data, time_value): 
    largest_index = root 
    left_child = (2 * root_index) + 2 
    right_child = (2 * root_index) + 1 

    if (left_child < size) and (data_list[root_index] < data_list[left_child]):
        largest_index = left_child
    
    if (right_child < size) and (data_list[root_index] < data_list[right_child]):
        largest_index = right_child
    
    if largest_index != root_index:
        _swap(data_list, root_index, largest_index)

        # heapify the root 
        heapify(data_list, size, largest_index, draw_data, time_value) 

    pass

def heap_sort(data_list, start, end, draw_data, time_value): 

    # building the max heap 
    for i in range((len(data_list) // 2) - 1, -1, -1): 
        heapify(data_list, len(data_list), i, draw_data, time_value)
    
    # does the sorting by extracting the roots 
    for i in range(len(data_list), 0, -1): 
        _swap(data_list, 0, i) 
        heapify(data_list, i, 0, draw_data, time_value) 
