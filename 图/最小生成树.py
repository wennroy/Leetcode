#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 返回最小的花费代价使得这n户人家连接起来
# @param n int整型 n户人家的村庄
# @param m int整型 m条路
# @param cost int整型二维数组 一维3个参数，表示连接1个村庄到另外1个村庄的花费的代价
# @return int整型
#
import math

# Prim算法版本，数据有问题
class Solution:
    def miniSpanningTree(self, n: int, m: int, cost: List[List[int]]) -> int:
        # write code here
        # 构建无向图，用邻接矩阵
        adjecent_matrix = [[math.inf] * n for _ in range(n)]
        for line in cost:
            adjecent_matrix[line[0] - 1][line[1] - 1] = line[2]
            adjecent_matrix[line[1] - 1][line[0] - 1] = line[2]
        for i in range(n):
            adjecent_matrix[i][i] = 0
        print(adjecent_matrix)
        # Prim算法
        closest = [0] * n
        lowest_cost = [0] * n

        for i, val in enumerate(adjecent_matrix[0]):
            lowest_cost[i] = val
        ans = 0
        for i in range(n - 1):
            min_pt = math.inf
            for j in range(n):
                if lowest_cost[j] and lowest_cost[j] < min_pt:
                    min_pt = lowest_cost[j]
                    idx = j
            ans += lowest_cost[idx]
            print(lowest_cost, closest)
            lowest_cost[idx] = 0
            for j in range(n):
                if lowest_cost[j] and adjecent_matrix[idx][j] < lowest_cost[j]:
                    lowest_cost[j] = adjecent_matrix[idx][j]
                    closest[j] = idx

        return ans


# 压缩并查集优化 - Kruskal算法 版本
class Union:
    def __init__(self, n: int):
        self.parent = [0 for _ in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.count = n
        for i in range(n + 1):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xi, yi = self.find(x), self.find(y)
        if xi == yi:
            return
        if self.rank[xi] > self.rank[yi]:
            self.parent[yi] = xi
            self.rank[xi] += self.rank[yi]
        else:
            self.parent[xi] = yi
            self.rank[yi] += self.rank[xi]
        self.count -= 1

    def connection(self, x, y):
        xi, yi = self.find(x), self.find(y)
        return xi == yi

    def count(self):
        return self.count


class Solution:
    def miniSpanningTree(self, n: int, m: int, cost: List[List[int]]) -> int:
        # write code here
        union = Union(n)
        cost.sort(key=lambda x: x[2])
        res = 0
        for a, b, w in cost:
            if union.connection(a, b):
                continue
            res += w
            union.union(a, b)
        return res
