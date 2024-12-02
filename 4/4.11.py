n = int(input())
s = (n+1)*n/2
k = 0
for i in range(1, n + 1):
    k += i
for i in range(n-1):
    k -= int(input())
print(k)
