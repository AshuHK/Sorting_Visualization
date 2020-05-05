import time 
from Swap import _swap

def insertion_sort(data_list, draw_data, time_value): 
    for i in range(1, len(data_list)): 
        j = i 

        while (j > 0) and (data_list[j] < data_list[j - 1]): 
            _swap(data_list, j, j - 1) 
            j -= 1 
