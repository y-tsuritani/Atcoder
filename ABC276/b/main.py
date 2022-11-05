N, M = map(int, input().split())
array = [[0] for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    array[i-1].append(j)
    array[j-1].append(i)

for k in array:
    if k == [0]:
        print(*k)
    else:
        k.remove(0)
        k.sort()
        k.insert(0, len(k))
        print(*k)