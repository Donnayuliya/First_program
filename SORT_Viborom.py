a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94]
n = len(a)
for i in range(n):
    a_min = min(a[:n])
    a.append(a_min)
    a.remove(a_min)
    n -= 1
print(a)