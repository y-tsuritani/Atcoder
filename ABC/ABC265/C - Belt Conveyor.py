h, w = map(int, input().split())

g = [[i for i in map(str, input().split())] for j in range(w)]
print(g)
viz = [[0 for i in range(h)] for j in range(w)]
print(viz)
i, j = 1, 1

while viz[i][j] == 1:
    print(i, j)
    if viz [i][j] == 1:
        print(-1)
        exit()
    viz[i][j] == 1
    if g[i][j] == 'U' and i != 0:
        i -= 1
    elif g[i][j] == 'D' and i != h-1:
        i += 1
    elif g[i][j] == 'L' and j != 0:
        j -= 1
    elif g[i][j] == 'R' and j != w-1:
        j += 1
    else:
        break
print(i+1, j+1)