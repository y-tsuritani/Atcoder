import itertools

n, m = map(int, input().split())
s, t = [], []
for _ in range(n):
    s.append(input())
for _ in range(m):
    t.append(input())

u_bar = ['_', '__', '___']

flg = False
for i in itertools.permutations(s):
    temp = '_'.join(i)
    if (temp not in t) and 3 <= len(temp) <= 16:
        flg = True
        print(temp)
        break
    else:
        flg = False

if flg: exit()
else: print(-1)



# 模範解答
import itertools

N,M=map(int,input().split())
S=[input() for _ in range(N)]
T=set([input() for _ in range(M)])
margin=16-sum(map(len,S))

#1個以上の"_"からなる長さLの列で、文字列長の和がS以下
def gen(L,S):
    if L==0:
        yield []
        return
    for i in range(1,S+1):
        for p in gen(L-1,S-i):
            yield ["_"*i]+p

for S_perm in itertools.permutations(S):
    for bar in gen(N-1,margin):
        temp=[""]*(2*N-1)
        temp[0::2]=S_perm
        temp[1::2]=bar
        ans="".join(temp)
    if len(ans)>=3 and ans not in T:
        print(ans)
        exit()

print("-1")
