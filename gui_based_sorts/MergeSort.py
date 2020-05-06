import time 

def merge(list1, list2, data_list, draw_data, time_value):
    i = 0
    j = 0

    while (i + j) < len(data_list):
        if (j == len(list2)) or ((i < len(list1)) and (list1[i] < list2[j])):
            data_list[i + j] = list1[i]
            i += 1

            # update colors here
        else:
            data_list[i + j] = list2[j]
            j += 1

            # update colors here too


def merge_sort(data_list, draw_data, time_value):
    if len(data_list) < 2: 
        return 

    middle_index = len(data_list) // 2 

    list1 = data_list[0:middle_index] 
    list2 = data_list[middle_index:len(data_list)]

    merge_sort(list1) 
    merge_sort(list2)

    merge(list1, list2, data_list, draw_data, time_value)
