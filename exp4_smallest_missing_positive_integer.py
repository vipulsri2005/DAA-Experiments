def smallest_missing_positive(arr):
    n = len(arr)

    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            index = arr[i] - 1
            arr[i], arr[index] = arr[index], arr[i]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1

arr = [3, 4, -1, 1]
print("Smallest missing positive integer:", smallest_missing_positive(arr))
