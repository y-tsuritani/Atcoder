import sys
import math
read = sys.stdin.read
nums = list(map(int, input().split()))
D, cst = 3, 998244353
left = math.prod(nums[:D])
right = math.prod(nums[D:])
result = (left - right) % cst
print(result)