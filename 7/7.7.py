k = 1
a = [int(i) for i in input().split()]
x = int(input())
for i in range(0, len(a)):
    if a[i] >= x:
        k+=1
print(k)
