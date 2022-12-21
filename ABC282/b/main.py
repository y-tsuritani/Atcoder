import itertools

def main() -> int:
    """
    B - Let's Get a Perfect Score
    https://atcoder.jp/contests/abc282/tasks/abc282_b
    output:
    二人が協力することで M 問全てを解くことが可能であるようなペアの個数を求める関数
    """
    n, m = map(int, input().split())
    S = [input() for i in range(n)]
    result = 0

    for si, sj in itertools.combinations(S,2):
        temp = [0]*m
        for i, moji in enumerate(si):
            if moji == "o":
                temp[i] = 1
            else:
                if sj[i] == "o":
                    temp [i] = 1
        if sum(temp) == m:
            result += 1
    
    return result

if __name__ == '__main__':
    result = main()
    print(result)