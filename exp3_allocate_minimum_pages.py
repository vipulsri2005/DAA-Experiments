def allocate_minimum_pages(pages, students):
    if students > len(pages):
        return -1

    def required_students(limit):
        count = 1
        current = 0

        for pages_count in pages:
            if current + pages_count <= limit:
                current += pages_count
            else:
                count += 1
                current = pages_count

        return count

    low = max(pages)
    high = sum(pages)

    while low < high:
        mid = (low + high) // 2

        if required_students(mid) <= students:
            high = mid
        else:
            low = mid + 1

    return low

pages = [12, 34, 67, 90]
students = 2
print("Minimum maximum pages:", allocate_minimum_pages(pages, students))
