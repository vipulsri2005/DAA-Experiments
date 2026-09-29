def kth_smallest(a, k):
    if len(a) <= 5:
        return sorted(a)[k - 1]

    medians = []
    for i in range(0, len(a), 5):
        group = sorted(a[i:i + 5])
        medians.append(group[len(group) // 2])

    pivot = kth_smallest(medians, (len(medians) + 1) // 2)
    left = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    if k <= len(left):
        return kth_smallest(left, k)
    if k <= len(left) + len(equal):
        return pivot
    return kth_smallest(right, k - len(left) - len(equal))

a = [7, 10, 4, 3, 20, 15]
print("Kth smallest element:", kth_smallest(a, 3))
