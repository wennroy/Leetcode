# 字典树 + 回溯
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 字典树 dictionary tree
        trie = {}
        for word in words:
            pt = trie
            for l in word:
                if l not in pt.keys():
                    pt[l] = {}
                pt = pt[l]
            pt['#'] = {}
        ans = set()
        m, n = len(board), len(board[0])
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 回溯
        def dfs(i, j, pt, visited, word):
            nonlocal ans
            if not pt or board[i][j] not in pt.keys():
                return
            pt = pt[board[i][j]]
            word += board[i][j]
            if '#' in pt.keys():
                ans.add(word)
            for x, y in DIRS:
                new_x, new_y = x + i, y + j
                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False:
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y, pt, visited, word)
                    visited[new_x][new_y] = False
            return

        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                dfs(i, j, trie, visited, "")
                visited[i][j] = False
        return list(ans)


# 一个字典树的快速写法的模板，找到一个单词就删除对应的部分
from functools import reduce
from collections import defaultdict as dc


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        Tree = lambda: dc(Tree)
        tree = Tree()
        for w in words: reduce(dict.__getitem__, w + '#', tree)
        res = []

        def dfs(used, x, y, dic, now):
            if '#' in dic:
                res.append(now)
                del dic['#']
            used.add((x, y))
            if x > 0 and (x - 1, y) not in used and board[x - 1][y] in dic:
                dfs(used, x - 1, y, dic[board[x - 1][y]], now + board[x - 1][y])
                if not dic[board[x - 1][y]]: del dic[board[x - 1][y]]
            if x < m - 1 and (x + 1, y) not in used and board[x + 1][y] in dic:
                dfs(used, x + 1, y, dic[board[x + 1][y]], now + board[x + 1][y])
                if not dic[board[x + 1][y]]: del dic[board[x + 1][y]]
            if y > 0 and (x, y - 1) not in used and board[x][y - 1] in dic:
                dfs(used, x, y - 1, dic[board[x][y - 1]], now + board[x][y - 1])
                if not dic[board[x][y - 1]]: del dic[board[x][y - 1]]
            if y < n - 1 and (x, y + 1) not in used and board[x][y + 1] in dic:
                dfs(used, x, y + 1, dic[board[x][y + 1]], now + board[x][y + 1])
                if not dic[board[x][y + 1]]: del dic[board[x][y + 1]]
            used.remove((x, y))

        for i in range(m):
            for j in range(n):
                if board[i][j] in tree:
                    dfs(set(), i, j, tree[board[i][j]], board[i][j])
                    if not tree[board[i][j]]: del tree[board[i][j]]
        return res

# 作者：thevan
# 链接：https://leetcode.cn/problems/word-search-ii/solution/python-32ms-100yong-shi-100nei-cun-zhan-yong-by-th/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
