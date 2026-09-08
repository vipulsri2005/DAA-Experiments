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

a = [1, 2, 4, 5]
b = [2, 3, 5, 6]
print("Intersection:", intersection_sorted_arrays(a, b))
