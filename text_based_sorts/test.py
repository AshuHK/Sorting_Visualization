# import the sorts here
from InsertionSort import insertion_sort

import random
import time

def test_insertion():
    """
    """
    test_list = [random.randint(0,1000) for i in range(1000)] 

    start_time = time.time()
    insertion_sort(test_list, 0, len(test_list) - 1 )

    # print(test_list == sorted(test_list))
    result_string = "" 
    if test_list == sorted(test_list): 
        result_string += "Test: Successful\t"
    else: 
        result_string += "Test: Fail\t" 
    
    result_string += "Insertion sort time: {} seconds".format(time.time() - start_time)

    print(result_string)

    pass

def test_selection():
    """
    """
    pass

def test_bubble():
    """
    """

    pass


def test_merge():
    """
    """

    pass


def test_quick():
    """
    """

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
