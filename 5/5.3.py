a = input()
b = len(a) // 2 + len(a) % 2
c = a[b:] + a[:b]
print(c)
