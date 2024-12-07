A = int(input())
a, b = 0, 1
c = 1
while A != b:
    a, b = b, a + b
    c += 1
    if A < b:
        c = -1
        break
print(c)
