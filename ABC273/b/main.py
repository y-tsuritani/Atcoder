#!/usr/bin/env python3
x, k = map(int, input().split())
for i in range(k):
    x //= 10**i
    if x % 10 >= 5:
        x += 10 - x % 10
    else:
        x -= x % 10
    x *= 10**i
print(x)