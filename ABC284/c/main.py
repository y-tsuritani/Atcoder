import sys

input = sys.stdin.readline


def DFS(graph: list, visit: list, target_vertex: int) -> None:
    """深さ優先探索

    Args:
        graph (list): 探索する無向グラフ
        visit (list): 各頂点の訪問済みフラグリスト
        target_vertex (int): ターゲットとなる頂点
    """
    visit[target_vertex] = True
    # ターゲットになる頂点の各ノードに対して未訪問か確認し、DFS を繰り返す
    for node in graph[target_vertex]:
        if not visit[node]:
            DFS(node)


# DFSを用いた解法
# 頂点数：vertex_num, 辺数：edge_num
vertex_num, edge_num = map(int, input().split())

graph = [[] for _ in range(vertex_num + 1)]
# 各頂点の訪問済みフラグの設定（デフォルトは未訪問）
visit = [0] * (vertex_num + 1)
Ans = 0
# 各辺が互いにつながってる頂点を自分のノードに追加する
for _ in range(edge_num):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

# index=0 の要素は探索に使用しない
for target_vertex in range(1, vertex_num + 1):
    # 頂点 i に訪問済みなら何もしない
    if visit[target_vertex]:
        continue
    Ans += 1
    DFS(graph, visit, target_vertex)
print(Ans)
