# import the sorts here
from InsertionSort import insertion_sort
from SelectionSort import selection_sort
from BubbleSort import bubble_sort
from QuickSort import quick_sort
from MergeSort import merge_sort

import random
import time


def generate_results(test_list, total_time, sort_type):
    """
    Takes the information from the test functions and builds the results
    into a string for readability

    :param test_list: Python list that is ideally sorted
    :param total_time: Time object that is total time of the sort
    :param sort_type: String of the done to get the result
    """

    result_str = ""
    if test_list == sorted(test_list):
        result_str += "Test: Successful\t"
    else:
        result_str += "Test: Fail\t"

    result_str += "{} sort time: {:5f} seconds".format(sort_type, total_time)

    return result_str


def test_insertion(user_int):
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    start_time = time.time()
    insertion_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Insertion")

    print(result_str)

    return None


def test_selection(user_int):
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    start_time = time.time()
    selection_sort(test_list)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "Selection")

    print(result_str)

    return None


def test_bubble(user_int):
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    start_time = time.time()
    bubble_sort(test_list)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "   Bubble")

    print(result_str)

    return None


def test_quick(user_int):
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    start_time = time.time()
    quick_sort(test_list, 0, len(test_list) - 1)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "    Quick")

    print(result_str)

    return None


def test_merge(user_int):
    test_list = [i for i in range(user_int)]
    random.shuffle(test_list)

    start_time = time.time()
    merge_sort(test_list)
    final_time = time.time()

    total_time = final_time - start_time
    result_str = generate_results(test_list, total_time, "    Merge")

    print(result_str)

    return None


def main():

    try:
        user_int = int(input("\nInput the size of the list to be generated: "))

        if user_int < 0:
            user_int *= -1

    except ValueError:
        user_int = 1000

    # just adding an empty line for readability
    print()

    test_insertion(user_int)
    test_selection(user_int)
    test_bubble(user_int)
    test_quick(user_int)
    test_merge(user_int)

    print()

    return None


if __name__ == "__main__":
    main()
