a = int(input())
b = 0
c = 1
d = 0
while a != 0:
    if b == a:
        c += 1
    else:
        if c > d:
           d = c
        c = 1
    b = a
    a = int(input())
if c > d:
    print(c)
else:
    print(d)
