n, k = map(int, input().split())
a = ['I']*n
for i in range(k):
    l, r = map(int, input().split())
    for j in range((l-1), (r)):
        a[j] = "."
for i in range(n):
    print(a[i], end = "")
