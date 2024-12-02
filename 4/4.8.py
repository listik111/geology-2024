n = int(input())
k = 1
t = 1
for i in range(2, n + 1):
    k *= i
    t += k
print(t)
