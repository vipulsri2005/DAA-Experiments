# Experiment 2 — Divide & Conquer on Arrays

def union_sorted_arrays(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            value = a[i]
            i += 1
        elif a[i] > b[j]:
            value = b[j]
            j += 1
        else:
            value = a[i]
            i += 1
            j += 1

        if not result or result[-1] != value:
            result.append(value)

    while i < len(a):
        if not result or result[-1] != a[i]:
            result.append(a[i])
        i += 1

    while j < len(b):
        if not result or result[-1] != b[j]:
            result.append(b[j])
        j += 1

    return result


def intersection_sorted_arrays(a, b):
    i = 0
    j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1

    return result


def search_rotated_sorted_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def count_inversions(arr):
    def merge_count(left, right):
        result = []
        i = 0
        j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                count += len(left) - i
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result, count

    def divide(a):
        if len(a) <= 1:
            return a, 0

        mid = len(a) // 2
        left, left_count = divide(a[:mid])
        right, right_count = divide(a[mid:])
        merged, split_count = merge_count(left, right)

        return merged, left_count + right_count + split_count

    _, count = divide(arr)
    return count


if __name__ == "__main__":
    a = [1, 2, 4, 5]
    b = [2, 3, 5, 6]

    print("Union:", union_sorted_arrays(a, b))
    print("Intersection:", intersection_sorted_arrays(a, b))

    arr = [4, 5, 6, 7, 0, 1, 2]
    print("Search in Rotated Sorted Array:", search_rotated_sorted_array(arr, 0))

    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Merge Sort:", merge_sort(arr))

    arr = [1, 20, 6, 4, 5]
    print("Count Inversions:", count_inversions(arr))
