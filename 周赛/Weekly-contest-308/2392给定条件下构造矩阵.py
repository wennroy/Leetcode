# 半个小时还是写出来了，拓扑排序

from collections import defaultdict


class Graph:
    def __init__(self, N):
        self.N = N
        self.inwards = defaultdict(list)
        self.outwards = defaultdict(list)

    def addEdge(self, u, v):
        self.outwards[u].append(v)
        self.inwards[v].append(u)

    def topologicalSort(self):
        stack = []
        res = []
        visited = [False] * self.N
        for i in range(self.N):
            if not self.inwards[i]:
                stack.append(i)
                res.append(i)

        while stack:
            pt = stack.pop()
            visited[pt] = True
            for i in self.outwards[pt]:
                self.inwards[i].remove(pt)
                if visited[i]:
                    return False
                if not self.inwards[i]:
                    stack.append(i)
                    res.append(i)
        if len(res) != self.N:  # 注意有时候入度为0的点可能是孤立点，10个点3个孤立点+7个两两结成的环，就会导致len(res)长度不够，应该返回False
            return False
        return res


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = Graph(k)
        for u, v in rowConditions:
            row_graph.addEdge(u - 1, v - 1)
        tp_row = row_graph.topologicalSort()
        if not tp_row:
            return []

        col_graph = Graph(k)
        for u, v in colConditions:
            col_graph.addEdge(u - 1, v - 1)
        tp_col = col_graph.topologicalSort()
        if not tp_col:
            return []

        ans = [[0] * k for _ in range(k)]
        map_list = [[0, 0] for _ in range(k)]
        for i in range(k):
            map_list[tp_row[i]][0] = i
            map_list[tp_col[i]][1] = i

        for i in range(k):
            ans[map_list[i][0]][map_list[i][1]] = i + 1

        return ans

# 利用一个in_deg数组来记录入度即可，不需要完全记录inwards
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges: List[List[int]]) -> List[int]:
            g = [[] for _ in range(k)]
            in_deg = [0] * k
            for x, y in edges:
                g[x - 1].append(y - 1)  # 顶点编号从 0 开始，方便计算
                in_deg[y - 1] += 1
            order = []
            q = deque(i for i, d in enumerate(in_deg) if d == 0)
            while q:
                x = q.popleft()
                order.append(x)
                for y in g[x]:
                    in_deg[y] -= 1
                    if in_deg[y] == 0:
                        q.append(y)
            return order if len(order) == k else None

        if (row := topo_sort(rowConditions)) is None or (col := topo_sort(colConditions)) is None:
            return []
        pos = {x: i for i, x in enumerate(col)}
        ans = [[0] * k for _ in range(k)]
        for i, x in enumerate(row):
            ans[i][pos[x]] = x + 1
        return ans

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/build-a-matrix-with-conditions/solution/by-endlesscheng-gpev/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。