n,*A = map(int,open(0).read().split())
L = sorted((a,i) for i,a in enumerate(A))[::-1]
S = set()
C = [0]*n
for a,i in L:
  C[len(S)-(a in S)] += 1
  S.add(a)
print(*C,sep="\n")