# import the sorts here
from InsertionSort import insertion_sort

import random
import time

def generate_results(test_list, total_time, sort_type): 
    result_str = ""
    if test_list == sorted(test_list): 
        result_str += "Test: Successful\t"
    else: 
        result_str += "Test: Fail\t"
    
    result_str += "{} sort time: {} seconds".format(sort_type, total_time) 

    return result_str

def test_insertion():
    test_list = [random.randint(0, 1000) for i in range(1000)]

    # time tracking of the sort
    start_time = time.time()
    insertion_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Insertion")

    print(result_str)

    return None


def test_selection():
    test_list = [random.randint(0, 1000) for i in range(1000)]

    # time tracking of the sort 
    start_time = time.time()
    selection_sort(test_list, 0, len(test_list) - 1) 
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Selection")

    return None 


def test_bubble():

    pass


def test_merge():

    pass


def test_quick():

    pass


def main():

    # just adding an empty line for readability
    print()

    test_selection()

    test_insertion()

    test_bubble()

    test_merge()

    test_quick()

    print()

    return None


if __name__ == "__main__":
    main()
