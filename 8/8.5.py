def f():
    s = int(input())
    if s != 0:
        f()
    print(s)
f()
