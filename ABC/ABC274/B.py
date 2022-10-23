h, w = map(int, input().split())
x = []
count = [0] * w
for i in range(h):
    row = list(input())
    x.append(row)
    for k, v in enumerate(row):
        if v == "#":
            count[k] += 1
print(" ".join(map(str, count)))