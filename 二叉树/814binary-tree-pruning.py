# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            if left == 0:
                root.left = None
            if right == 0:
                root.right = None
            if left == 0 and right == 0 and root.val == 0:
                return 0
            else:
                return 1

        if dfs(root) == 0:
            return None
        return root

