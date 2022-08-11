# DFS直接解答
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def total_val(num):
            ans = 0
            while num >= 10:
                ans += num % 10
                num = num // 10
            return ans + num

        direction = [(1, 0), (0, 1)]
        visited = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            temp = total_val(i) + total_val(j)
            if temp > k:
                return 0
            ans = 1
            visited[i][j] = 1
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                if 0 <= x <= m - 1 and 0 <= y <= n - 1 and visited[x][y] == -1:
                    ans += dfs(x, y)
            return ans

        return dfs(0, 0)


# 标答BFS
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 标答二：递推 其实也算是动态规划

def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/ji-qi-ren-de-yun-dong-fan-wei-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。