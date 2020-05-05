import time 
from Swap import _swap

def bubble_sort(data_list, draw_data): 
    for i in range(len(data_list)): 
        for j in range(len(data_list) - 1, i, -1): 
            if data_list[j] < data_list[j - 1]: 
                _swap(data_list, j, j - 1)
                draw_data(data_list)
                time.sleep(0.2)
