def main() -> list:
    """
    output:

    """
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    words.reverse()  # 破壊的処理
    return words


if __name__ == "__main__":
    words = main()
    for word in words:
        print(word)
