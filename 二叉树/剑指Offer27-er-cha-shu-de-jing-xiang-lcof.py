# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        new_head = TreeNode(root.val)
        new_head.left = self.mirrorTree(root.right)
        new_head.right = self.mirrorTree(root.left)
        return new_head

