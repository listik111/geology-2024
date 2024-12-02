k = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        k+=1
m = len(a) - k
print(m)
