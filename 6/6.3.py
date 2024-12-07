N = int(input())
x = 1
a = 0
while N >= x * 2:
    x *= 2
    a += 1
print(a, x)