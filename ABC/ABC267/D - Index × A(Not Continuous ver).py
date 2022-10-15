import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
inf = pow(10, 18) + 1
dp0 = [0] * 1
for i in range(n):
    dp = list(dp0)
    dp.append(-inf)
    ai = a[i]
    for j in range(1, i + 2):
        dp[j] = max(dp[j], dp0[j - 1] + j * ai)
    dp0 = dp
ans = dp[m]
print(ans)