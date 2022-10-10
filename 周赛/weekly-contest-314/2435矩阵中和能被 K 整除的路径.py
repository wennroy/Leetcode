# 三维DP
# 数字过大，溢出错误

from typing import List
MOD_NUM = 1e9 + 7
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j][k] 从开始到第i行第j列除以k余的路径数目
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]%k] = 1
        for i in range(m):
            for j in range(n):
                for l in range(k):
                    val = grid[i][j] % k
                    if i >= 1:
                        dp[i][j][l] += dp[i-1][j][(k+l-val)%k]
                    if j >= 1:
                        dp[i][j][l] += dp[i][j-1][(k+l-val)%k]
                    dp[i][j][l] %= MOD_NUM
        return int(dp[-1][-1][0] % MOD_NUM)


grid = [[5,2,4],[3,0,5],[0,7,2]]
k = 3
sol = Solution()
print(sol.numberOfPaths(grid, k))