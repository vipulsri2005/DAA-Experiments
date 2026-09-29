import heapq

arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
heap = []

for i, a in enumerate(arrays):
    heapq.heappush(heap, (a[0], i, 0))

result = []
while heap:
    value, i, j = heapq.heappop(heap)
    result.append(value)
    if j + 1 < len(arrays[i]):
        heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

print("Merged array:", result)
