def main() -> int:
    """
    D - Factorial and Multiple
    https://atcoder.jp/contests/ABC280/tasks/abc280_d
    与えられた整数を素因数分解して最大値を返す関数
    """
    k = int(input())
    a = prime_factorize(k)
    result = max(a)
    return result

def prime_factorize(n:int) -> list:
    """
    素因数分解してリストを返す関数
    """
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == '__main__':
    result = main()
    print(result)