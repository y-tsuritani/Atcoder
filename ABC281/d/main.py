import itertools

def main() -> int:
    """
    D - Max Multiple
    https://atcoder.jp/contests/ABC281/tasks/abc281_d
    output:
    S に含まれる D の倍数の最大値を求める関数
    """
    n, k, d = map(int, input().split())
    num_list = list(map(int, input().split()))
    combi = [sum(x) for x in itertools.combinations(num_list, k)]
    combi.sort(reverse=True)
    result = -1
    for i in combi:
        if i % d == 0:
            result = i
            break
    return result

if __name__ == '__main__':
    result = main()
    print(result)