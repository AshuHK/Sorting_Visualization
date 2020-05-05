import time 
from Swap import _swap

def selection_sort(data_list, draw_data, time_value): 
    for i in range(len(data_list)): 
        min_index = i 

        for j in range(i + 1, len(data_list)): 
            if data_list[min_index] > data_list[j]: 
                min_index = j 
        
        _swap(data_list, i, min_index) 

        color_list = ["red" for x in range(len(data_list))]

        for x in range(len(color_list)): 
            if (x == i) or (x == min_index): 
                color_list[x] = "green"
        
        draw_data(data_list, color_list) 
        time.sleep(time_value) 
    
    draw_data(data_list, ["green" for i in range(len(data_list))])
