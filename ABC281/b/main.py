import re

def main() -> bool:
    """
    B - Sandwich Number
    https://atcoder.jp/contests/ABC281/tasks/abc281_b
    output:
    英大文字+数字6桁+英大文字であるかを判定する関数
    """
    s = input()
    pattern = r'[A-Z][1-9][0-9]{5}[A-Z]'
    res = re.match(pattern, s)
    result = "No"
    if res:
        result = "Yes"
    return result

if __name__ == '__main__':
    result = main()
    print(result)