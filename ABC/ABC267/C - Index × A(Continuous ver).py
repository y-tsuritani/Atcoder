import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in a:
    s.append(s[-1] + i)

now = 0
for i in range(m - 1):
    now += a[i] * (i + 1)

inf = pow(10, 18) + 1
ans = -inf
for i in range(m - 1, n):
    now += a[i] * m
    ans = max(ans, now)
    now -= s[i + 1] - s[i - m + 1]
print(ans)