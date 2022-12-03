N, K = map(int, input().split())
A = list(map(int, input().split()))

if K > N:
    result = [0]*N
else:
    result = A[K-N:]+[0]*K

print(*result)