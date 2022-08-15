# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def dfs_find(self, root, p, q):
        if not root:
            return False

        left = self.dfs_find(root.left, p, q)
        right = self.dfs_find(root.right, p, q)
        if left and right:
            self.ans = root
            return False
        if root == p or root == q:
            if left or right:
                self.ans = root
                return False
            return True
        else:
            return left or right

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs_find(root, q, p)
        return self.ans

