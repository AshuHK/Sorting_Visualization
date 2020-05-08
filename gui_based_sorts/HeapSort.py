import time
from Swap import _swap


def heapify(data_list, size, root_index, draw_data, time_value):
    """
    Heapifies the list and visualizes the steps 
    Expected Complexity (heapify only): O(log(n)) (time) and O(1) (space) 

    :param data_list: 
    :param size: 
    :param root_index: 
    :param draw_data: 
    :param time_value: 
    """
    largest_index = root_index
    left_index = (2 * root_index) + 1
    right_index = (2 * root_index) + 2

    if (left_index < size) and (data_list[root_index] < data_list[left_index]):
        largest_index = left_index

    if (right_index < size) and (data_list[largest_index] < data_list[right_index]):
        largest_index = right_index

    if largest_index != root_index:
        _swap(data_list, root_index, largest_index)

        color_list = ["red" for x in range(len(data_list))]

        for x in range(len(color_list)):
            if (x == root_index) or (x == largest_index):
                color_list[x] = "blue"

        draw_data(data_list, color_list)
        time.sleep(time_value)

        heapify(data_list, size, largest_index, draw_data, time_value)


def heap_sort(data_list, draw_data, time_value):

    for i in range((len(data_list) // 2) - 1, -1, -1):
        heapify(data_list, len(data_list), i, draw_data, time_value)

    draw_data(data_list, ["blue" for i in range(len(data_list))])

    for i in range(len(data_list) - 1, 0, -1):
        _swap(data_list, i, 0)

        # show color here for swaps
        color_list = ["red" for x in range(len(data_list))]

        for x in range(len(color_list)):
            if (x == i) or (x == 0):
                color_list[x] = "green"

        draw_data(data_list, color_list)
        time.sleep(time_value)

        heapify(data_list, i, 0, draw_data, time_value)

    draw_data(data_list, ["green" for i in range(len(data_list))])
