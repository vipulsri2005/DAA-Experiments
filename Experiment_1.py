# Experiment 1 — Sorting Fundamentals

def insertion_sort_iterative(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    a = arr[:]

    if n <= 1:
        return a

    a = insertion_sort_recursive(a, n - 1)
    key = a[n - 1]
    j = n - 2

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key

    return a


def dutch_national_flag(arr):
    a = arr[:]
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        elif a[mid] == 2:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
        else:
            raise ValueError("Array must contain only 0, 1, and 2.")

    return a


def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Insertion Sort - Iterative:", insertion_sort_iterative(arr))

    arr = [12, 11, 13, 5, 6]
    print("Insertion Sort - Recursive:", insertion_sort_recursive(arr))

    arr = [2, 0, 2, 1, 1, 0]
    print("Dutch National Flag:", dutch_national_flag(arr))

    arr = [2, 2, 1, 1, 2, 2, 2]
    print("Majority Element:", majority_element(arr))
