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

a = [1, 2, 4, 5]
b = [2, 3, 5, 6]
print("Union:", union_sorted_arrays(a, b))
