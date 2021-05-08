import random


def bubble_sort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
    return array


def FindSmallestElement(arr):
    smallestelem = arr[0]
    ind_smallel = 0
    for i in range(1, len(arr)):
        if arr[i] <= smallestelem:
            smallestelem = arr[i]
            ind_smallel = i
    return ind_smallel


# Sorting by choice
def sort_choice(arr):
    new_arr = []
    for i in range(len(arr)):
        ind_smal = FindSmallestElement(arr)
        new_arr.append(arr.pop(ind_smal))
    return new_arr


# Sorting by inserts
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        while (j >= 0 and temp < array[j]):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = temp
    return array


# Procedure for converting a subtree to a binary heap with the root node root_index
def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]
        heapify(array, heap_size, largest)


# The main function for sorting an array of a given size(pyramid sorting)
def heap_sort(array):
    n = len(array)
    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        left = [i for i in array[1:] if i <= pivot]
        right = [k for k in array[1:] if k > pivot]
    return quicksort(left) + [pivot] + quicksort(right)


if __name__ == '__main__':
    test_array = [random.randint(-100, 100) for _ in range(10)]
    print('Initial list:\n', test_array)
    print('Sorting results:')
    print(heap_sort(test_array))
    print(insertion_sort(test_array))
    print(quicksort(test_array))
    print(bubble_sort(test_array))
    print(sort_choice(test_array))

