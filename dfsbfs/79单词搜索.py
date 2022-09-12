# 暴力搜索DFS
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        word_len = len(word)

        def dfs(i, j, step):
            if board[i][j] != word[step]:
                return False
            if step == word_len - 1:
                return True
            traveled[i][j] = True
            for x, y in DIR:
                new_x = x + i
                new_y = y + j
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and traveled[new_x][new_y] == False:
                    if dfs(new_x, new_y, step + 1):
                        return True
                    traveled[new_x][new_y] = False
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                traveled = [[False] * n for _ in range(m)]
                if dfs(i, j, 0):
                    return True

        return False

# 标答的回溯
# 几乎一样
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / word - search / solution / dan - ci - sou - suo - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。