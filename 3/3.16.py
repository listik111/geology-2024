p = int(input())
x = int(input())
y = int(input())
s = 100 * x + y
x = int(s * (100 + p) / 100)
print(x // 100, x % 100)
