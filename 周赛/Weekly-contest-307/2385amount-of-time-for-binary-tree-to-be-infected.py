# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 构架无向图，再进行遍历。时间复杂度O(2n)，空间复杂度O(n)，会稍微久一点

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        from collections import defaultdict
        if not root.left and not root.right:
            return 0

        # 构建无向图
        nxtLevel = [root]
        vectors = defaultdict(list)
        while nxtLevel:
            curLevel = nxtLevel
            nxtLevel = []
            for node in curLevel:
                if node.left:
                    vectors[node].append(node.left)
                    vectors[node.left].append(node)
                    nxtLevel.append(node.left)
                if node.right:
                    vectors[node].append(node.right)
                    vectors[node.right].append(node)
                    nxtLevel.append(node.right)

        # 利用DFS寻找：
        visited = defaultdict(lambda :False)
        def dfs(pt):
            visited[pt] = True
            ans = -1
            for nxt_pt in vectors[pt]:
                if not visited[nxt_pt]:
                    ans = max(ans, dfs(nxt_pt))

            return ans + 1

        for node in vectors.keys():
            if node.val == start:
                return dfs(node)


# 不构建无向图的方法，直接DFS返回两个值进行判断。一次遍历即可
# 时间复杂度O(n)，空间复杂度O(1)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(root, start):  # 返回[距离start的距离，到叶子结点的深度]
            if not root.left and not root.right:
                if root.val == start:
                    return [0, 0]
                else:
                    return [-1, 0]
            res_left, res_right = [-1, -1], [-1, -1]
            if root.left:
                res_left = dfs(root.left, start)
            if root.right:
                res_right = dfs(root.right, start)

            if root.val == start:
                max_step = max(res_left[1], res_right[1]) + 1
                return [0, max_step]

            if res_left[0] != -1:
                max_step = max(res_left[0] + res_right[1] + 2, res_left[1])  # 右侧的结点多走两格
                return [res_left[0] + 1, max_step]

            elif res_right[0] != -1:
                max_step = max(res_right[0] + res_left[1] + 2, res_right[1])  # 左侧的结点多走两格
                return [res_right[0] + 1, max_step]

            max_step = max(res_left[1], res_right[1]) + 1
            return [-1, max_step]

        ans = dfs(root, start)
        return ans[1]
