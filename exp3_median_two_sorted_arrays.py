def median_of_two_sorted_arrays(a, b):
    if len(a) > len(b):
        return median_of_two_sorted_arrays(b, a)

    m = len(a)
    n = len(b)
    low = 0
    high = m

    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i

        left_a = float("-inf") if i == 0 else a[i - 1]
        right_a = float("inf") if i == m else a[i]
        left_b = float("-inf") if j == 0 else b[j - 1]
        right_b = float("inf") if j == n else b[j]

        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 0:
                return (max(left_a, left_b) + min(right_a, right_b)) / 2
            return max(left_a, left_b)

        if left_a > right_b:
            high = i - 1
        else:
            low = i + 1

a = [1, 3]
b = [2, 4]
print("Median:", median_of_two_sorted_arrays(a, b))
