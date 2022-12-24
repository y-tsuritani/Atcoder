n = int(input())
A = [0] + list(map(int, input().split()))
q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A[query[1]] = query[2]
    elif query[0] == 2:
        print(A[query[1]])

