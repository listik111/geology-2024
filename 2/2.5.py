x1 = int(input())
x2 = int(input())
x3 = int(input())
if x2 >= x1 and x3 >= x1:
    print(x1)
elif x1 >= x2 and x3 >= x2:
    print(x2)
else:
    print(x3)
