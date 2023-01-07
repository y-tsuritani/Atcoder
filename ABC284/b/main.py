t = int(input())
for _ in range(t):
    nums = []
    n = int(input())
    nums = map(int, input().split())
    odd_cnt = 0
    for i in nums:
        if i % 2 == 1:
            odd_cnt += 1
    print(odd_cnt)
