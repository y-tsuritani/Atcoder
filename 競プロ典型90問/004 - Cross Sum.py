import itertools

# 入力を受け取る
H, W = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

# 行方向、列方向の合計値を産出
rows_sum = map(sum, A)
columns_Sum = map(sum, zip(*A))

print(A)
print(list(rows_sum))
print(list(columns_Sum))

result = []
for i, j  in itertools.combinations(rows_sum, columns_Sum):
    result.append(i + j)

print(result)
