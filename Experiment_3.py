# Experiment 3 — Divide & Conquer: Matrices and Selection

import random


def matrix_multiply_brute_force(A, B):
    n = len(A)
    m = len(B)
    p = len(B[0])

    if len(A[0]) != m:
        raise ValueError("Incompatible matrix dimensions.")

    C = [[0] * p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]

    return C


def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def subtract_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def next_power_of_two(n):
    size = 1
    while size < n:
        size *= 2
    return size


def pad_matrix(A, size):
    padded = [[0] * size for _ in range(size)]
    for i in range(len(A)):
        for j in range(len(A[0])):
            padded[i][j] = A[i][j]
    return padded


def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, subtract_matrix(B12, B22))
    M4 = strassen(A22, subtract_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))

    C11 = add_matrix(subtract_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(subtract_matrix(add_matrix(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C


def strassen_matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Incompatible matrix dimensions.")

    rows = len(A)
    cols = len(B[0])
    common = len(B)

    size = next_power_of_two(max(rows, cols, common))
    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)

    C = strassen(A_padded, B_padded)

    return [row[:cols] for row in C[:rows]]


def allocate_minimum_pages(pages, students):
    if students > len(pages):
        return -1

    low = max(pages)
    high = sum(pages)

    def can_allocate(limit):
        count = 1
        current = 0

        for pages_count in pages:
            if current + pages_count <= limit:
                current += pages_count
            else:
                count += 1
                current = pages_count

                if count > students:
                    return False

        return True

    while low < high:
        mid = (low + high) // 2

        if can_allocate(mid):
            high = mid
        else:
            low = mid + 1

    return low


def randomized_quick_sort(arr):
    a = arr[:]

    def partition(low, high):
        pivot_index = random.randint(low, high)
        a[pivot_index], a[high] = a[high], a[pivot_index]
        pivot = a[high]

        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def quick_sort(low, high):
        if low < high:
            pivot = partition(low, high)
            quick_sort(low, pivot - 1)
            quick_sort(pivot + 1, high)

    quick_sort(0, len(a) - 1)
    return a


def median_two_sorted_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a

    m = len(a)
    n = len(b)
    low = 0
    high = m

    while low <= high:
        partition_a = (low + high) // 2
        partition_b = (m + n + 1) // 2 - partition_a

        max_left_a = float("-inf") if partition_a == 0 else a[partition_a - 1]
        min_right_a = float("inf") if partition_a == m else a[partition_a]

        max_left_b = float("-inf") if partition_b == 0 else b[partition_b - 1]
        min_right_b = float("inf") if partition_b == n else b[partition_b]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) +
                        min(min_right_a, min_right_b)) / 2
            return max(max_left_a, max_left_b)

        if max_left_a > min_right_b:
            high = partition_a - 1
        else:
            low = partition_a + 1

    raise ValueError("Input arrays must be sorted.")


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    print("Matrix Multiplication - Brute Force:")
    print(matrix_multiply_brute_force(A, B))

    print("Strassen Matrix Multiplication:")
    print(strassen_matrix_multiply(A, B))

    pages = [12, 34, 67, 90]
    print("Allocate Minimum Pages:", allocate_minimum_pages(pages, 2))

    arr = [10, 7, 8, 9, 1, 5]
    print("Randomized Quick Sort:", randomized_quick_sort(arr))

    a = [1, 3]
    b = [2]
    print("Median of Two Sorted Arrays:", median_two_sorted_arrays(a, b))
