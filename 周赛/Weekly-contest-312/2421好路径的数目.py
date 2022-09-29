# https://leetcode.cn/problems/number-of-good-paths/

# 祭上超时版本。强行记忆化DFS。
from sortedcontainers import SortedDict
from collections import defaultdict
from typing import List

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        if not edges:
            return len(vals)
        V = len(edges)
        outward = defaultdict(list)
        for i in range(V):
            outward[edges[i][0]].append(edges[i][1])
            outward[edges[i][1]].append(edges[i][0])

        n = len(vals)
        visited = [False] * n

        def dfs(i, max_val):
            nonlocal cur_idx
            ans = 0
            if record and max_val == vals[i]:
                record_same[i] = cur_idx
                ans += 1
            record.add(i)
            for nxt_pt in outward[i]:
                if nxt_pt not in record and vals[nxt_pt] <= max_val:
                    ans += dfs(nxt_pt, max_val)
            return ans

        res = 0
        record_same = dict()
        dfs_record = dict()
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                cur_idx = i
                record = set()
                if cur_idx in record_same.keys():
                    cur_dfs = dfs_record[record_same[cur_idx]]
                else:
                    cur_dfs = dfs(i, vals[i])
                    dfs_record[i] = cur_dfs
                res += cur_dfs
        res = res // 2
        return n + res


# 并查集
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        # 并查集模板
        fa = list(range(n))
        # size[x] 表示节点值等于 vals[x] 的节点个数，如果按照节点值从小到大合并，size[x] 也是连通块内的等于最大节点值的节点个数
        size = [1] * n
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = n
        for vx, x in sorted(zip(vals, range(n))):
            fx = find(x)
            for y in g[x]:
                y = find(y)
                if y == fx or vals[y] > vx: continue  # 只考虑最大节点值比 vx 小的连通块
                if vals[y] == vx:  # 可以构成好路径
                    ans += size[fx] * size[y]  # 乘法原理
                    size[fx] += size[y]  # 统计连通块内节点值等于 vx 的节点个数
                fa[y] = fx  # 把小的节点值合并到大的节点值上
        return ans

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/number-of-good-paths/solution/bing-cha-ji-by-endlesscheng-tbz8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。