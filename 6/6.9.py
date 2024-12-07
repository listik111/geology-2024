i = 0
max = 0
k = 0
N = int(input())
while N != 0:
    if max < N:
        max = N
        k = i
    N = int(input())
    i += 1
print(k)
