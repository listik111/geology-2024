from math import sqrt

k = 0
p = 0
x = int(input())
n = 0
while x != 0:
    n += 1
    k += x
    p += x ** 2
    x = int(input())
print(sqrt((p - k ** 2 / n) / (n - 1)))
