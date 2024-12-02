n = input()
if n.count('f') > 1:
    t = n.find('f',n.find('f')+1)
    print(t)
if n.count('f') == 1:
    print(-1)
if n.count('f') == 0:
    print(-2)
