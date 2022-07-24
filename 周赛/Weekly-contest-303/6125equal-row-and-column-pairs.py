# 暴力解法，用numpy计算是否相等

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        import numpy as np
        n = len(grid)
        grid = np.array(grid)
        ans = 0
        for i in range(n):
            for j in range(n):
                if all(grid[:,i] == grid[j,:]):
                    ans += 1
        return ans