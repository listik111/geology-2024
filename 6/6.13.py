k = int(input())
m = 0
i = 1
while k != 0:
    if k > m:
        m = k
        i = 1
    elif k == m:
        i+=1
    k=int(input())
print(i)
