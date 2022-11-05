import sys
read = sys.stdin.read
S = input()
result = []
for i, s in enumerate(S):
    if s == 'a':
        result.append(i+1)
if result:
    print(max(result))
else:
    print(-1)