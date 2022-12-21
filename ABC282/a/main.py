def main() -> int:
    """
    A - Generalized ABC
    https://atcoder.jp/contests/abc282/tasks/abc282_a
    output:
    入力された文字アルファベットを出力する関数
    """
    k = int(input())
    uppers = [chr(i) for i in range(65,65+26)]
    result = uppers[:k]
    return result

if __name__ == '__main__':
    result = main()
    print("".join(result))