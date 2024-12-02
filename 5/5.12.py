s = input()
p = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = p + s[i]
        print(t, end = '')
