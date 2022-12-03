def main() -> int:
    """
    コマが置かれているマスの個数を整数で出力せよ。
    """
    h, w = map(int, input().split())
    result = 0
    for _ in range(h):
        s = input()
        for i in s:
            if i == '#':
                result += 1
            else:
                pass
    return result

if __name__ == '__main__':
    result = main()
    print(result)