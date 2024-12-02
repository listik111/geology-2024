n=int(input())
m=int(input())
x=int(input())
y=int(input())
if n<m:
    x1=n-x
    y1=m-y
else:
    x1=m-x
    y1=n-y
if x<x1 and x<y1 and x<y:
    print(x)
if y<x and y<y1 and y<x1:
    print(y)
if x1<x and x1<y1 and x1<y:
    print(x1)
if y1<y and y1<x and y1<x1:
    print(y1)