def kth_largest(arr, k):
    if k < 1 or k > len(arr):
        return -1

    target = len(arr) - k
    left = 0
    right = len(arr) - 1

    while left <= right:
        pivot = arr[right]
        index = left

        for i in range(left, right):
            if arr[i] <= pivot:
                arr[index], arr[i] = arr[i], arr[index]
                index += 1

        arr[index], arr[right] = arr[right], arr[index]

        if index == target:
            return arr[index]
        elif index < target:
            left = index + 1
        else:
            right = index - 1

    return -1

arr = [3, 2, 1, 5, 6, 4]
k = 2
print("Kth largest element:", kth_largest(arr, k))
