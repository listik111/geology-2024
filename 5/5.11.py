n = input()
n = n.replace('h','*',1)
n = n[::-1]
n = n.replace('h','*',1)
n = n.replace('h','H')
n = n.replace('*','h')
n = n[::-1]
print(n)
