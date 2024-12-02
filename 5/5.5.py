n = input()
if n.count('f') == 1:
    s = n.find('f')
    print(s)
elif n.count('f') >= 1:
    s = n.find('f')
    e = n.rfind('f')
    print(s, e)
