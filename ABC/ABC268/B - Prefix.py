s = input()
t = input()

flg = False
result = t.find(s)
if result == 0:
    flg = True

if flg: print('Yes')
else: print('No')