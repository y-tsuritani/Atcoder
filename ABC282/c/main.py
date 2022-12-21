def main() -> str:
    """
    C - String Delimiter
    https://atcoder.jp/contests/ABC282/tasks/abc282_c
    output:
    ""で括られていない,を.に変換する関数
    """
    h = int(input())
    s = input()
    result_list = []
    score = 0
    for i in s:
        if i == '"':
            score += 1
        elif i == ",":
            # TODO：if文をネストしているのでTLEになってしまう
            if score%2 == 0:
                i = "."
        result_list.append(i)
        result = "".join(result_list)
    return result

if __name__ == '__main__':
    result = main()
    print(result)

