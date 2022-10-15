# Step #1. Input
N, K = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]
flag = True

# Step #2. Check Difference
diff = 0
for i, j in zip(A, B):
    diff += abs(i-j)
if diff > K:
    flag = False

# Step #3. Check Parity
if diff % 2 != K % 2:
    flag = False

if flag: print('Yes')
else: print('No')