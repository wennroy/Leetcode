# 层次遍历 或 BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nxtLevel = [root]
        while nxtLevel:
            curLevel = nxtLevel
            nxtLevel = []
            for node in curLevel:
                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
        ans = 0
        for node in curLevel:
            ans += node.val
        return ans

# 可以用队列来存储
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            ans = 0
            for _ in range(len(q)):
                node = q.popleft()
                ans += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/deepest-leaves-sum/solution/ceng-shu-zui-shen-xie-zi-jie-dian-de-he-by-leetc-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 当然也能写DFS
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxLevel, ans = -1, 0
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if node is None:
                return
            nonlocal maxLevel, ans
            if level > maxLevel:
                maxLevel, ans = level, node.val
            elif level == maxLevel:
                ans += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/deepest-leaves-sum/solution/ceng-shu-zui-shen-xie-zi-jie-dian-de-he-by-leetc-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。