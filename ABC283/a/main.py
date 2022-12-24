def main() -> int:
    """
    output:

    """
    a, b = map(int, input().split())
    result = a ** b
    return result

if __name__ == '__main__':
    result = main()
    print(result)