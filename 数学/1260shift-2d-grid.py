class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        volumne = m*n
        k = k % (volumne)
        import numpy as np
        import copy
        grid = np.array(grid)
        values = copy.deepcopy(grid.reshape((1,-1))[0])
        count = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = values[count-k]
                count+=1
        return grid.tolist()


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                index1 = (i * n + j + k) % (m * n)
                ans[index1 // n][index1 % n] = v
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/shift-2d-grid/solution/er-wei-wang-ge-qian-yi-by-leetcode-solut-ploz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。