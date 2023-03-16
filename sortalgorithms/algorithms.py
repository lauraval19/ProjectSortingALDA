"""
    Author: Laura Alvarado
    Project Sorting
"""


def selection_sort(arr):
    """Builds the final sorted array or list with sorting algorithm called selection sort
    @param array to sort
    @return array sorted
    Complexity: O(n^2)
    """
    for i in range(0, len(arr)):
        minimun_position = i
        for j in range(i + 1, len(arr)):
            if arr[minimun_position] > arr[j]:
                minimun_position = j
        arr[i], arr[minimun_position] = arr[minimun_position], arr[i]
    print(arr)
    return arr


def merge_sort(arr):
    """Builds the final sorted array or list with sorting algorithm called merge sort
    @param array to sort
    Complexity: nlog(n)
    """
    if len(arr) == 1:
        return arr

    middle_arr = len(arr) // 2
    left_arr = arr[:middle_arr]
    right_arr = arr[middle_arr:]

    sorted_left_array = merge_sort(left_arr)
    sorted_right_array = merge_sort(right_arr)

    return merge_arrays(sorted_left_array, sorted_right_array)


def merge_arrays(left_arr, right_arr):
    """
    merge two arrays to sort
    @Param left_arr first middle of array
    @Param second_arr second middle of array
    """
    sorted_arr = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            sorted_arr.append(right_arr[0])
            right_arr.pop(0)
        else:
            sorted_arr.append(left_arr[0])
            left_arr.pop(0)
    while len(left_arr) > 0:
        sorted_arr.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        sorted_arr.append(right_arr[0])
        right_arr.pop(0)
    return sorted_arr


def insertion_sort(arr):
    """
    Builds the final sorted array or list with sorting algorithm called merge sort
    @param array to sort
    Complexity: O(n^2)
    """
    for i in range(1, len(arr)):
        temp_value = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > temp_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp_value
    return arr
