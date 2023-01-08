import math
import sys
from typing import List, Tuple

input = sys.stdin.readline


def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())

        p = 0
        q = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i != 0:
                continue
            if (n / i) % i == 0:
                p = i
                q = n / i / i
            else:
                q = i
                p = round(math.sqrt(n / i))
            break
        print(f"{p} {q}")


if __name__ == "__main__":
    main()
