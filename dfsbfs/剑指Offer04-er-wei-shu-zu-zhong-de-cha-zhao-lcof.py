# 复习了一边DFSBFS，但这题为啥要用这方法呢呜呜
px = [1, 0]
py = [0, 1]

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        if m == 0:
            return False
        visited = [[0]*m for _ in range(n)]
        def dfs(i: int, j: int) -> bool:
            visited[i][j] = 1
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                return False
            for k in range(2):
                x = i + px[k]
                y = j + py[k]
                if x < n and y < m and visited[x][y] == 0:
                    if dfs(x,y):
                        return True

            return False

        return dfs(0,0)

# 暴力循环查找 比DFS 快30ms
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
            else:
                continue
        return False

# 线性查找

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        j = 0
        while i >= 0 and j <= len(matrix[0]) - 1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False

'''
lass Solution {
    public boolean findNumberIn2DArray(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int rows = matrix.length, columns = matrix[0].length;
        int row = 0, column = columns - 1;
        while (row < rows && column >= 0) {
            int num = matrix[row][column];
            if (num == target) {
                return true;
            } else if (num > target) {
                column--;
            } else {
                row++;
            }
        }
        return false;
    }
}

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/solution/mian-shi-ti-04-er-wei-shu-zu-zhong-de-cha-zhao-b-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''