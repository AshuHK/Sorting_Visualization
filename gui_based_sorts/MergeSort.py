import time


def merge(data_list, start, middle, end, draw_data, time_value):
    """
    Merges the sublist of the array and visualize the step
    Expected Complexity (Merge only): O(n*log(n)) (time) and O(n) (space) 

    :param data_list: Python list to merged 
    :param start: Integer for the starting index in the list 
    :param middle: Integer for the middle index in the list 
    :param end: Integer for the ending index in the list 
    :param draw_data: Function written in main.py to visualize the steps 
    :param time_value: Float based on the input for the time between steps
    """

    # visualize the sub list found and wait the specified amount of time 
    draw_data(data_list, get_color_list(len(data_list), start, middle, end))
    time.sleep(time_value)

    # seperate the list in half 
    start_list = data_list[start : middle + 1]
    end_list = data_list[middle + 1 : end + 1]

    left_index = 0
    right_index = 0

    for i in range(start, end + 1):
        # does the merging for the two halves of the sublists  
        if left_index < len(start_list) and right_index < len(end_list):
            if start_list[left_index] <= end_list[right_index]:
                data_list[i] = start_list[left_index]
                left_index += 1
            else:
                data_list[i] = end_list[right_index]
                right_index += 1

        elif left_index < len(start_list):
            data_list[i] = start_list[left_index]
            left_index += 1
        else:
            data_list[i] = end_list[right_index]
            right_index += 1

    # generate the color list to be visualized 
    color_list = ["red" for i in range(len(data_list))]

    # color the values being placed back in the original list green
    for i in range(len(color_list)):
        if (i >= start) and (i <= end):
            color_list[i] = "green"
    
    # visualize the step and wait for the specified amount of time 
    draw_data(data_list, color_list)
    time.sleep(time_value)


def merge_sort(data_list, start, end, draw_data, time_value):
    if start >= end:
        return

    middle_index = (start + end) // 2

    # sort the first half of the data
    merge_sort(data_list, start, middle_index, draw_data, time_value)

    # sort the second half of the data
    merge_sort(data_list, middle_index + 1, end, draw_data, time_value)

    # combine the two halves 
    merge(data_list, start, middle_index, end, draw_data, time_value)


def get_color_list(length, start, middle, end):
    color_list = []

    for i in range(length):
        if (i >= start) and (i <= end):
            if (i >= start) and (i <= middle):
                color_list.append("blue")
            else:
                color_list.append("orange")
        else:
            color_list.append("red")

    return color_list
