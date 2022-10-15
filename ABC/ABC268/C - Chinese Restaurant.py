from collections import deque

n = int(input())
p = deque(map(int, input().split()))

p_plesure = 0
for _ in range(n):
    c_plesure = 0
    temp = p.pop()
    p.insert(0, temp)
    for x in p:
        if p.index(x) in ((x-1)%n, x, (x+1)%n):
            c_plesure += 1
    p_plesure = max(p_plesure, c_plesure)
    if c_plesure == n: break
print(p_plesure)


# 模範解答
N=int(input())
P=list(map(int,input().split()))

A=[0]*N

for i,p in enumerate(P):
    A[(i-p-1)%N]+=1
    A[(i-p  )%N]+=1
    A[(i-p+1)%N]+=1

print(max(A))
