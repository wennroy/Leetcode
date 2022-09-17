# 模拟下落过程即可
from typing import List
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # 模拟遍历，时间复杂度O(mn)，空间复杂度O(1)
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        # 第 j 个球
        for j in range(n):
            row = 0
            col = j
            while row < m:
                if grid[row][col] == 1:
                    if col == n - 1 or grid[row][col + 1] == -1:
                        break
                    col += 1
                    row += 1
                elif grid[row][col] == -1:
                    if col == 0 or grid[row][col - 1] == 1:
                        break
                    col -= 1
                    row += 1
            ans[j] = col if row == m else -1

        return ans