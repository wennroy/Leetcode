# 改样例了，时间一下就上去了
# 正常DFS，可以先利用COUNTER来排除就不可能的board
# Counter(word) - Counter(chain(*board)): 只会计算Counter(word)有的字母，如果不为空，则说明board没有全部包含，直接return False

from collections import Counter
from itertools import chain


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if Counter(word) - Counter(chain(*board)):  # counter returns a hash table with key(elem):value(counts)
            return False  # if board is only as big as word, return false

        m, n = len(board), len(board[0])
        word_len = len(word)
        visited = [[-1] * n for _ in range(m)]
        PX = [-1, 1, 0, 0]
        PY = [0, 0, 1, -1]
        def dfs(i, j, k = 0):
            if board[i][j] != word[k]:
                return False
            visited[i][j] = k
            if k == word_len-1:
                return True
            for l in range(4):
                x = PX[l] + i
                y = PY[l] + j

                if 0 <= x <= m-1 and 0 <= y <= n-1 and visited[x][y] == -1:
                    if dfs(x, y, k+1):
                        return True
            visited[i][j] = -1
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    return True
        return False


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if Counter(word) - Counter(chain(*board)):  # counter returns a hash table with key(elem):value(counts)
            return False  # if board is only as big as word, return false

        def DFS(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = DFS(i - 1, j, k + 1) or DFS(i + 1, j, k + 1) or DFS(i, j - 1, k + 1) or DFS(i, j + 1, k + 1)
            board[i][j] = word[k]
            return res

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if word[0] == board[i][j] and DFS(i, j, 0):
                    return True
        return False