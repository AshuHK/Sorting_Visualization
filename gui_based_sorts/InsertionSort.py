import time 
from Swap import _swap

def insertion_sort(data_list, draw_data, time_value): 
    for i in range(1, len(data_list)): 
        j = i 

        while (j > 0) and (data_list[j] < data_list[j - 1]): 
            _swap(data_list, j, j - 1) 
            j -= 1 

            color_list = ["red" for x in range(len(data_list))] 

            for x in range(len(color_list)): 
                if (x == j) or (x == j - 1): 
                    color_list[x] = "green" 
            
            draw_data(data_list, color_list) 
            time.sleep(time_value) 
    
    draw_data(data_list, ["green" for i in range(len(data_list))])
