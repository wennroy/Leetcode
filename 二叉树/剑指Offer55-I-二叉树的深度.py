# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs_depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return max(dfs_depth(root.left), dfs_depth(root.right)) + 1
        return dfs_depth(root)

# 标答：
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/solution/er-cha-shu-de-shen-du-by-leetcode-soluti-dk8c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。