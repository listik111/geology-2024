n = int(input())
a = 0
b = 1
m = 0
c = 0
if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n > 1:
    while m != n -1:
        c = a + b
        a, b = b, c
        m += 1
    print(c)
