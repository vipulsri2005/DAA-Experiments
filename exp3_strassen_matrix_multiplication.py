def add_matrix(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

def subtract_matrix(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]

def strassen(a, b):
    n = len(a)

    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    p1 = strassen(a11, subtract_matrix(b12, b22))
    p2 = strassen(add_matrix(a11, a12), b22)
    p3 = strassen(add_matrix(a21, a22), b11)
    p4 = strassen(a22, subtract_matrix(b21, b11))
    p5 = strassen(add_matrix(a11, a22), add_matrix(b11, b22))
    p6 = strassen(subtract_matrix(a12, a22), add_matrix(b21, b22))
    p7 = strassen(subtract_matrix(a11, a21), add_matrix(b11, b12))

    c11 = add_matrix(subtract_matrix(add_matrix(p5, p4), p2), p6)
    c12 = add_matrix(p1, p2)
    c21 = add_matrix(p3, p4)
    c22 = subtract_matrix(subtract_matrix(add_matrix(p5, p1), p3), p7)

    result = []
    for i in range(mid):
        result.append(c11[i] + c12[i])
    for i in range(mid):
        result.append(c21[i] + c22[i])

    return result

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

result = strassen(a, b)

for row in result:
    print(row)
