# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot
        if root.right:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        root.right = TreeNode(val)
        return root
