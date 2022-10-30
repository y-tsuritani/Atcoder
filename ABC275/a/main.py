import sys
read = sys.stdin.read
N = int(input())
nums = [x for x in map(int, input().split())]

print(nums.index(max(nums))+1)