# 直接暴力计算，n <= 100
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n - 2) for _ in range(m - 2)]

        def max_local_area(x, y):
            max_val = 0
            for i in range(3):
                for j in range(3):
                    if grid[x + i][y + j] > max_val:
                        max_val = grid[x + i][y + j]
            return max_val

        for j in range(n - 2):
            for i in range(m - 2):
                dp[i][j] = max_local_area(i, j)

        return dp

