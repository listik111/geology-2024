n = 8
x = []
y = []
for i in range(n):
    k, s = [int(s) for s in input().split()]
    x.append(k)
    y.append(s)
t = 1
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            t = 0
if t == 1:
    print('NO')
else:
    print('YES')
