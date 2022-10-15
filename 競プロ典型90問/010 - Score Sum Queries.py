def cumsum(xs):
    result = [xs[0]]
    for x in xs[1:]:
        result.append(result[-1] + x)
    return result


N = int(input())
s =[list(map(int, input().split())) for i in range(N)]
class1 = [0] + [0 if s[i][0] == 2 else s[i][1] for i in range(N)]
class2 = [0] + [0 if s[i][0] == 1 else s[i][1] for i in range(N)]

csum_1 = cumsum(class1)
csum_2 = cumsum(class2)

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    result_c1 = csum_1[R]-csum_1[L-1]
    result_c2 = csum_2[R]-csum_2[L-1]
    print(f'{result_c1} {result_c2}')