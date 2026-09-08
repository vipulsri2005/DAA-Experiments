def merge_and_count(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    arr[left:right + 1] = temp
    return count

def count_inversions(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    count = count_inversions(arr, left, mid)
    count += count_inversions(arr, mid + 1, right)
    count += merge_and_count(arr, left, mid, right)

    return count

arr = [1, 20, 6, 4, 5]
print("Inversions:", count_inversions(arr, 0, len(arr) - 1))
