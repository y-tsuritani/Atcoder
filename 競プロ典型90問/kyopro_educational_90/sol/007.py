from bisect import bisect_left
N = int(input())
*A, = map(int, input().split())
Q = int(input())
A.sort()
for _ in range(Q):
    b = int(input())
    i = bisect_left(A, b)
    u = 10**18
    if i < N:
        u = min(u, abs(A[i] - b))
    if i > 0:
        u = min(u, abs(A[i - 1] - b))
    print(u)
