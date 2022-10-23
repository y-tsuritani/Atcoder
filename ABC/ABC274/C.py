n = int(input())
A = list(map(int, input().split()))
depth = [0, 0]

# i = 0, child -> 2, 3
# i = 1, child -> 4, 5

for i in range(n):
    a = A[i]
    depth.append(depth[a] + 1)
    depth.append(depth[a] + 1)

for i in range(1, 2*n+2):
    print(depth[i])