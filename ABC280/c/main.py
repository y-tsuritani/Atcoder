def main() -> int:
    """
    output:
    答えを出力せよ。なお、答えが複数考えられる場合はどれを出力しても正解となる。
    """
    s = input()
    t = input()
    result = 1
    for i,j in zip(s, t):
        if i == j:
            result += 1
        else:
            break
    return result

if __name__ == '__main__':
    result = main()
    print(result)