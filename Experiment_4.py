# Experiment 4 — Selection & Recursive Techniques

def maximum_product(arr):
    if len(arr) < 2:
        raise ValueError("At least two elements are required.")

    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")

    for num in arr:
        if num >= largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

        if num <= smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num

    return max(largest * second_largest, smallest * second_smallest)


def kth_largest_quickselect(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("Invalid value of k.")

    a = arr[:]
    target = len(a) - k

    def partition(left, right):
        pivot = a[right]
        i = left

        for j in range(left, right):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1

        a[i], a[right] = a[right], a[i]
        return i

    left = 0
    right = len(a) - 1

    while left <= right:
        pivot_index = partition(left, right)

        if pivot_index == target:
            return a[pivot_index]
        elif pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

    return -1


def fibonacci_recursive(n):
    if n < 0:
        raise ValueError("n must be non-negative.")

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_dp(n):
    if n < 0:
        raise ValueError("n must be non-negative.")

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def smallest_missing_positive(arr):
    a = arr[:]
    n = len(a)

    for i in range(n):
        while 1 <= a[i] <= n and a[a[i] - 1] != a[i]:
            correct_index = a[i] - 1
            a[i], a[correct_index] = a[correct_index], a[i]

    for i in range(n):
        if a[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -2]
    print("Maximum Product:", maximum_product(arr))

    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print("Kth Largest Element:", kth_largest_quickselect(arr, k))

    n = 10
    print("Fibonacci - Recursion:", fibonacci_recursive(n))
    print("Fibonacci - Dynamic Programming:", fibonacci_dp(n))

    arr = [3, 4, -1, 1]
    print("Smallest Missing Positive Integer:", smallest_missing_positive(arr))
