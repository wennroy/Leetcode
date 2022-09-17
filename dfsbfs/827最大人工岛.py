# 两遍遍历，求出结果
from typing import List
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        traveled = [[False] * n for _ in range(m)]
        island_area = [[0] * n for _ in range(m)]
        group = [[-1] * n for _ in range(m)]
        group_num = 0
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            traveled[i][j] = True
            cur_record.append((i, j))
            step = 1
            for x, y in DIR:
                new_x, new_y = i + x, j + y
                if 0 <= new_x < m and 0 <= new_y < n and traveled[new_x][new_y] == False:
                    step += dfs(new_x, new_y)

            return step

        max_ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and traveled[i][j] == False:
                    cur_record = []
                    ans = dfs(i, j)
                    max_ans = max(ans, max_ans)
                    for x, y in cur_record:
                        island_area[x][y] = ans
                        group[x][y] = group_num
                    group_num += 1

        def check(i, j):
            ans = 0
            cur_group = []
            for x, y in DIR:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < m and 0 <= new_y < n and group[new_x][new_y] not in cur_group:
                    cur_group.append(group[new_x][new_y])
                    ans += island_area[new_x][new_y]

            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    max_ans = max(check(i, j) + 1, max_ans)

        return max_ans

# 标答，基本是一致的思路
from collections import Counter
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0] * n for _ in range(n)]
        area = Counter()
        def dfs(i: int, j: int) -> None:
            tag[i][j] = t
            area[t] += 1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 四个方向
                if 0 <= x < n and 0 <= y < n and grid[x][y] and tag[x][y] == 0:
                    dfs(x, y)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x and tag[i][j] == 0:  # 枚举没有访问过的陆地
                    t = i * n + j + 1
                    dfs(i, j)
        ans = max(area.values(), default=0)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:  # 枚举可以添加陆地的位置
                    new_area = 1
                    connected = {0}
                    for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):  # 四个方向
                        if 0 <= x < n and 0 <= y < n and tag[x][y] not in connected:
                            new_area += area[tag[x][y]]
                            connected.add(tag[x][y])
                    ans = max(ans, new_area)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/making-a-large-island/solution/zui-da-ren-gong-dao-by-leetcode-solution-lehy/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法二：也可以使用并查集
# 但个人认为并查集效果并不是特别的好


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 并查集
        fa = [[(i, j) for j in range(n)] for i in range(n)]
        size = [[1 for j in range(n)] for i in range(n)]

        def unionSet(i1, j1, i2, j2, fa, size):
            ancestor1 = find(i1, j1, fa)
            ancestor2 = find(i2, j2, fa)
            if ancestor1 == ancestor2:
                return
            # 按秩合并
            if size[ancestor1[0]][ancestor1[1]] > size[ancestor2[0]][ancestor2[1]]:
                ancestor1, ancestor2 = ancestor2, ancestor1
            fa[ancestor1[0]][ancestor1[1]] = ancestor2
            size[ancestor2[0]][ancestor2[1]] += size[ancestor1[0]][ancestor1[1]]
            size[ancestor1[0]][ancestor1[1]] = -1

        def find(i, j, fa):
            i_stack = []
            j_stack = []
            while fa[i][j] != (i, j):
                i_stack.append(i)
                j_stack.append(j)
                i, j = fa[i][j]
            # 路径压缩
            while i_stack or j_stack:
                fa[i_stack.pop()][j_stack.pop()] = (i, j)
            return (i, j)

        # 候选的0格子们
        candidates = []

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    # 只需要和右侧，下侧的格子并起来就无遗漏无重复了（其实有重复也不影响正确性，重要的是无遗漏）
                    if 0 <= i + 1 < n and grid[i + 1][j]:
                        unionSet(i, j, i + 1, j, fa, size)
                    if 0 <= j + 1 < n and grid[i][j + 1]:
                        unionSet(i, j, i, j + 1, fa, size)
                else:
                    candidates.append((i, j))

        # 初始大小
        ans = max(map(max, size))

        for i, j in candidates:
            # 检查上下左右有几个联通分量
            ancestors = set()
            if 0 <= i + 1 < n and grid[i + 1][j]:
                ancestors.add(find(i + 1, j, fa))
            if 0 <= i - 1 < n and grid[i - 1][j]:
                ancestors.add(find(i - 1, j, fa))
            if 0 <= j + 1 < n and grid[i][j + 1]:
                ancestors.add(find(i, j + 1, fa))
            if 0 <= j - 1 < n and grid[i][j - 1]:
                ancestors.add(find(i, j - 1, fa))
            # 相邻的各个联通分量大小之和再加上自己的一格
            curr_size = sum(map(lambda x: size[x[0]][x[1]], ancestors)) + 1
            ans = max(ans, curr_size)

        return ans


# 作者：isuxiz
# 链接：https: // leetcode.cn / problems / making - a - large - island / solution / by - isuxiz - eihf /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class UnionFind:  # 默写并查集模板
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]

    def Find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x: int, y: int) -> bool:
        root_x = self.Find(x)
        root_y = self.Find(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True

    def inthesamepart(self, x: int, y: int) -> bool:
        return self.Find(x) == self.Find(y)

    def getpartsize(self, x: int) -> int:
        root_x = self.Find(x)
        return self.size[root_x]


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        UF = UnionFind(R * C)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:  # 初始化并查集  把陆地都连接在一起
                    for dr, dc in ((1, 0), (0, 1)):
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                            UF.Union(r * C + c, nr * C + nc)
        res = max(UF.size)  # 当前最大的区域
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:  # 按照题意  把一块海洋，变成陆地
                    tmp = 1  # 当前这块就 + 1
                    root_set = set()
                    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):  # 4个方向  最多有可能连接4块区域
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:  # 在矩阵内 且是陆地
                            part_root = UF.Find(nr * C + nc)
                            if part_root not in root_set:  # 且还没统计过
                                tmp += UF.size[part_root]
                                root_set.add(part_root)
                    res = max(res, tmp)
        return res


# 作者：code_learner
# 链接：https: // leetcode.cn / problems / making - a - large - island / solution / c - python3 - tao - bing - cha - ji - mo - ban - mo - xie - w40z2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。