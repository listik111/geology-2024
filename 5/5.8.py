s = input()
print(s[:s.find('h')]+s[s.rfind('h'):s.find('h'):-1]+'h'+s[s.rfind('h')+1:])
