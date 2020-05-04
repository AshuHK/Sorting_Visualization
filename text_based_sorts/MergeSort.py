def merge(list1, list2, unsorted):
    """
    """
    i = 0
    j = 0

    while i + j < len(unsorted):
        if (j == len(list2)) or (i < len(list1) and list1[i] < list2[j]):
            unsorted[i + j] = list1[i]
            i += 1
        else:
            unsorted[i + j] = list2[j]
            j += 1
    pass


def merge_sort(unsorted):
    """
    """
    if len(unsorted) < 2:
        return

    middle_index = len(unsorted) // 2

    list1 = unsorted[0:middle_index]
    list2 = unsorted[middle_index : len(unsorted)]

    merge_sort(list1)
    merge_sort(list2)

    merge(list1, list2, unsorted)
