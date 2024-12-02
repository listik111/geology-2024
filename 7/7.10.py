a = [int(s) for s in input().split()]
x = max(a)
y = min(a)
t1 = a.index(x)
t2 = a.index(y)
a[t1] = y
a[t2] = x
print(' '.join(str(i) for i in a))
