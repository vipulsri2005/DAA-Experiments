from collections import Counter

s = "aaabbc"
c = Counter(s)
result = ""
prev = ""

while c:
    x = max((k for k in c if k != prev), key=c.get, default=None)
    if x is None:
        print("Not possible")
        break
    result += x
    c[x] -= 1
    if c[x] == 0:
        del c[x]
    prev = x
else:
    print("Rearranged string:", result)
