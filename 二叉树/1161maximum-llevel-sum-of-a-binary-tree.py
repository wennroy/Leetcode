# 简单的二叉树DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.level = []

        def dfs(self, root, depth):
            if not root:
                return None
            if len(self.level) < depth + 1:
                self.level.append(root.val)
            else:
                self.level[depth] += root.val
            dfs(self, root.left, depth + 1)
            dfs(self, root.right, depth + 1)

        dfs(self, root, 0)

        max_val = -inf
        ind = 0
        for i, val in enumerate(self.level):
            if val > max_val:
                max_val = val
                ind = i

        return ind + 1

# BFS
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        ans = []
        q = deque([root])
        level = 0
        while q:
            level += 1
            level_sum = 0
            # 遍历完当前层, 新 append 的一定是下一层的
            for i in range(len(q)):
                curr = q.popleft()
                level_sum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level_sum > max_sum:
                max_sum = level_sum
                ans = [level]
            elif level_sum == max_sum:
                ans.append(level)
        return min(ans)

# 作者：isuxiz
# 链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/solution/by-isuxiz-6ro9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum = []
        def dfs(node: TreeNode, level: int) -> None:
            if level == len(sum):
                sum.append(node.val)
            else:
                sum[level] += node.val
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        dfs(root, 0)
        return sum.index(max(sum)) + 1  # 层号从 1 开始

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/solution/zui-da-ceng-nei-yuan-su-he-by-leetcode-s-2tm4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, maxSum = 1, root.val
        level, q = 1, [root]
        while q:
            sum, nq = 0, []
            for node in q:
                sum += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            if sum > maxSum:
                ans, maxSum = level, sum
            q = nq
            level += 1
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/solution/zui-da-ceng-nei-yuan-su-he-by-leetcode-s-2tm4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。