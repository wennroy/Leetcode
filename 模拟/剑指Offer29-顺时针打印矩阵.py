# 直接强行模拟，好处是空间复杂度O(1)，但时间复杂度可能会略慢，多个if elif判断
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        i = j = 0
        up = left = 0
        down, right = m - 1, n - 1
        ans = []
        left_flag = right_flag = up_flag = down_flag = True

        while down >= up and left <= right:
            ans.append(matrix[i][j])

            if i == up and up_flag:
                if j == right:
                    up += 1
                    i += 1
                    right_flag = True
                    up_flag = False
                else:
                    j += 1
            elif j == right and right_flag:
                if i == down:
                    right -= 1
                    j -= 1
                    down_flag = True
                    right_flag = False
                else:
                    i += 1
            elif i == down and down_flag:
                if j == left:
                    down -= 1
                    i -= 1
                    left_flag = True
                    down_flag = False
                else:
                    j -= 1
            elif j == left and left_flag:
                if i == up:
                    left += 1
                    j += 1
                    up_flag = True
                    left_flag = False
                else:
                    i -= 1

        return ans

# 直接模拟，可以用visited记录访问过的空间，遇到不可前进的障碍，就转90度
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / shun - shi - zhen - da - yin - ju - zhen - lcof / solution / shun - shi - zhen - da - yin - ju - zhen - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 大佬写法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            print(matrix)
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res


# 按层模拟，走完一圈再缩小空间，这样就不用暴力if else写了。

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / shun - shi - zhen - da - yin - ju - zhen - lcof / solution / shun - shi - zhen - da - yin - ju - zhen - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。