import sys

input = sys.stdin.readline

# Union-Find (素集合データ構造) を用いた解法
# 頂点数：vertex_num, 辺数：edge_num
vertex_num, edge_num = map(int, input().split())
# UnionFind

Group = [i for i in range(vertex_num + 1)]  # グループ分け
Nodes = [1] * (vertex_num + 1)  # 各グループのノードの数


def find(x: int) -> int:
    """要素 x を含む集合の名前を返す関数

    Args:
        x (int): 要素 x

    Returns:
        int: 要素 x を含む
    """
    while Group[x] != x:
        x = Group[x]
    return x


def union(x: int, y: int) -> None:
    """集合 x と集合 y を併合、名前を x もしくは y とする

    Args:
        x (int): 集合 x 
        y (int): 集合 y
    """
    if find(x) != find(y):
        if Nodes[find(x)] < Nodes[find(y)]:

            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)

        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)

# 辺 i が結ぶ頂点 u と頂点 v が与えられる
for i in range(edge_num):
    ver_u, ver_v = map(int, input().split())
    union(ver_u, ver_v)

ANS = 0
# 要素 i について
for i in range(1, vertex_num + 1):
    if find(i) == i:
        ANS += 1

print(ANS)
