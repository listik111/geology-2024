x1 = int(input())
y1 = int(input())
z1 = int(input())
x2 = int(input())
y2 = int(input())
z2 = int(input())
s1 = x1 * 3600 + y1 * 60 + z1
s2 = x2 * 3600 + y2 * 60 + z2
ds = s2 - s1
print(ds)
