import itertools

def main() -> int:
    """
    C - Circular Playlist
    https://atcoder.jp/contests/ABC281/tasks/abc281_c
    output:
    t秒後に何曲目の何秒かを返す関数
    """
    n, t = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    accum_list = [0] + [i for i in itertools.accumulate(A)]
    t = t % accum_list[-1]
    result = [t-x for x in accum_list if t-x > 0]
    return result

if __name__ == '__main__':
    result = main()
    print(f'{result.index(result[-1])+1} {result[-1]}')