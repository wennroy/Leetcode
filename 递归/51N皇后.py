class Solution:
    def __init__(self):
        self.ans = []

    def checkValid(self, pos: List[int], row: int, col: int) -> bool:
        for i in range(row):
            if col == pos[i] or abs(row - i) == abs(col - pos[i]):
                return False

        return True

    def rec(self, n: int, row: int, pos: List[int], res: int) -> int:
        if row == n:
            temp = [['.'] * n for _ in range(n)]
            for i, p in enumerate(pos):
                temp[i][p] = 'Q'
                temp[i] = ''.join(temp[i])
            self.ans.append(temp)
            return res
        for i in range(n):
            if self.checkValid(pos, row, i):
                pos[row] = i
                res = self.rec(n, row + 1, pos, res)
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        pos = [-1] * n
        res = self.rec(n, 0, pos, 0)
        return self.ans


# 按位操作的解法
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def solve(row: int, columns: int, diagonals1: int, diagonals2: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2))
                while availablePositions:
                    position = availablePositions & (-availablePositions)
                    availablePositions = availablePositions & (availablePositions - 1)
                    column = bin(position - 1).count("1")
                    queens[row] = column
                    solve(row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1)

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        solve(0, 0, 0, 0)
        return solutions

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


