import random

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

def randomized_quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot - 1)
        randomized_quick_sort(arr, pivot + 1, high)

arr = [10, 7, 8, 9, 1, 5]
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
