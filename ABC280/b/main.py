def main() -> list:
    """
    output:
    全ての条件を満たす数列 A=(A1,…,AN) の各要素を、順に空白区切りで出力せよ。
    """
    n =int(input())
    s = list(map(int, input().split()))
    sum, result = s[0], [s[0]]
    for i in s[1:]:
        result.append(i-sum)
        sum = i    
    return result

if __name__ == '__main__':
    result = main()
    print(*result)