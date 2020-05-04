from Swap import _swap


def selection_sort(unsorted):
    """
    Does an selection sort on a Python list
    Expected Complexity: O(n^2) (time) and O(1) (space)

    :param unsorted: unsorted Python list to be sorted
    """
    for i in range(len(unsorted)):

        min_index = i
        for j in range(i + 1, len(unsorted)):
            if unsorted[min_index] > unsorted[j]:
                min_index = j

        _swap(unsorted, i, min_index)
