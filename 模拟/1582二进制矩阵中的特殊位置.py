class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rowsum, colsum = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                rowsum[i] += mat[i][j]
                colsum[j] += mat[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                if rowsum[i] == 1 and colsum[j] == 1 and mat[i][j] == 1:
                    ans += 1

        return ans

# 求一个二维数组的行列和
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)]
        res = 0
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 1 and rows_sum[i] == 1 and cols_sum[j] == 1:
                    res += 1
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/special-positions-in-a-binary-matrix/solution/er-jin-zhi-ju-zhen-zhong-de-te-shu-wei-z-kan4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。