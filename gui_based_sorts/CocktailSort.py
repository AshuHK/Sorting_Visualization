import time
from Swap import _swap


def cocktail_sort(data_list, draw_data, time_value):
    """
    Does a cocktail sort on a list and visualze the sort 
    Expected Complexity (Sort Only): O(n^2) (time) and O(1) (space) 

    :param data_list: Python list to be sorted 
    :param draw_data: function written in main.py that visualizes the list 
    :param time_value: Float based on the input for time between each step
    """

    # declare and initalize basic variables
    swapped_bool = True
    start_index = 0
    end_index = len(data_list) - 1

    while swapped_bool == True:
        swapped_bool = False
        
        # similar to bubble sort, moves the largest values to the top 
        for i in range(start_index, end_index):
            if data_list[i] > data_list[i + 1]:
                _swap(data_list, i, i + 1)
                
                # generate the color list for the visualization function
                color_list = ["red" for i in range(len(data_list))]

                # color the two elements being swapped green 
                for x in range(len(color_list)):
                    if (x == i) or (x == i + 1):
                        color_list[x] = "blue"

                # visualize the step
                draw_data(data_list, color_list)
                time.sleep(time_value)

                swapped_bool = True

        if swapped_bool == False:
            break

        swapped_bool = False

        end_index -= 1

        for i in range(end_index - 1, start_index - 1, -1):
            if data_list[i] > data_list[i + 1]:
                _swap(data_list, i, i + 1)

                color_list = ["red" for i in range(len(data_list))]

                for x in range(len(color_list)):
                    if (x == i) or (x == i + 1):
                        color_list[x] = "orange"

                draw_data(data_list, color_list)
                time.sleep(time_value)

                swapped_bool = True

        start_index += 1

    draw_data(data_list, ["green" for i in range(len(data_list))])
