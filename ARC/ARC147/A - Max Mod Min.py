from collections import deque


N = int(input())
A = list(map(int, input().split()))
cnt = 0

A = sorted(A, reverse = True)
D = deque(A)

while len(D) > 1:
    cnt += 1
    i = D[0]
    j = D[-1]
    idx = D.index(i)
    D[idx] = i % j
    if D[idx] == 0:
        D.remove(D[idx])
    elif D[idx] <= D[-1]:
        D.append(D.pop())

print(cnt)
