def maximum_product(arr):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")

    for value in arr:
        if value >= largest:
            second_largest = largest
            largest = value
        elif value > second_largest:
            second_largest = value

        if value <= smallest:
            second_smallest = smallest
            smallest = value
        elif value < second_smallest:
            second_smallest = value

    return max(largest * second_largest, smallest * second_smallest)

arr = [-10, -3, 5, 6, -2]
print("Maximum product:", maximum_product(arr))
