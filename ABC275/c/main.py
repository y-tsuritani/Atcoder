import sys
import itertools
read = sys.stdin.read
grids = [0] * 9
for i in range(9):
    grids[i] = list(map(str, input().split()))
for i, j in 