def main() -> list:
    """
    A - Count Down
    https://atcoder.jp/contests/abc281/tasks/abc281_a
    output:
    N 以下の非負整数を大きい方から順にすべて出力する関数
    """
    n = int(input())
    result = [x for x in range(n+1)]
    result.sort(reverse=True)
    return result

if __name__ == '__main__':
    result = main()
    for x in result:
        print(x)