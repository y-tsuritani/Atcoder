# 入力を受け取る
P = []
for _ in range(4):
    P.append(list(map(int, input().split())))

# 各頂点への2直線のベクトルを求める
flag = True
for i in range(4):
    v1 = [P[(i+1)%4][0] - P[i][0], P[(i+1)%4][1] - P[i][1]]
    v2 = [P[(i+2)%4][0] - P[i][0], P[(i+2)%4][1] - P[i][1]]
    # ベクトルの外積
    judge = v1[0]*v2[1] - v1[1]*v2[0]

    if judge < 0:
        flag = False

# 結果の出力        
if flag: print('Yes')
else: print('No')
