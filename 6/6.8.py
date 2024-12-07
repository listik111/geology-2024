x = int(input())
k = 0
while x != 0:
    if x > k:
        k = x
    x = int(input())
print(k)