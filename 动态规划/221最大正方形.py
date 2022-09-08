# 改进暴力法
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_len = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i + max_len >= m or matrix[i + max_len][j] == '0':
                        continue
                    if j + max_len >= n or matrix[i][j + max_len] == '0':
                        continue
                    if matrix[i + max_len][j + max_len] == '0':
                        continue
                cur_len = 0
                x, y = i, j
                is_square = True
                while x < m and y < n and matrix[x][y] == '1':
                    for check_x in range(i, x):
                        if matrix[check_x][y] == '0':
                            is_square = False

                    for check_y in range(j, y):
                        if matrix[x][check_y] == '0':
                            is_square = False

                    if not is_square:
                        break

                    cur_len += 1
                    x += 1
                    y += 1

                max_len = max(max_len, cur_len)

        return max_len ** 2

# 时间复杂度 O(mn k^2)，空间复杂度O(1)

# 标答的暴力法超时
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    # 遇到一个 1 作为正方形的左上角
                    maxSide = max(maxSide, 1)
                    # 计算可能的最大正方形边长
                    currentMaxSide = min(rows - i, columns - j)
                    for k in range(1, currentMaxSide):
                        # 判断新增的一行一列是否均为 1
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        for m in range(k):
                            if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                                flag = False
                                break
                        if flag:
                            maxSide = max(maxSide, k + 1)
                        else:
                            break

        maxSquare = maxSide * maxSide
        return maxSquare


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / maximal - square / solution / zui - da - zheng - fang - xing - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 动态规划的方法

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # dp 以这个点为正方形右下角，已有的正方形最长边长

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                        continue
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        flattened_dp = [j for sub in dp for j in sub]
        return max(flattened_dp) ** 2