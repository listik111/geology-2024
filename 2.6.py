x1 = int(input())
x2 = int(input())
x3 = int(input())
if x1 == x2 and x2 == x3 and x1 == x3:
    print('3')
elif x1 == x2 or x2 == x3 or x3 == x1:
    print('2')
if x1 != x2 and x2 != x3 and x3 != x1:
    print('0')
