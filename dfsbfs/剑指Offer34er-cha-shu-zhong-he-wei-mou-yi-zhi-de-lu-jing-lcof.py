# 读错题了，简单DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedDict
from bisect import bisect_left


class Solution:
    def __init__(self):
        self.sumval_node = SortedDict()

    def recu_tree(self, root, prev_val, prev_path):
        if not root.left and not root.right:
            if prev_val + root.val not in self.sumval_node.keys():
                self.sumval_node[prev_val + root.val] = [prev_path + [root.val]]
            else:
                self.sumval_node[prev_val + root.val].append(prev_path + [root.val])
            return

        if root.left:
            self.recu_tree(root.left, prev_val + root.val, prev_path + [root.val])  # 0 stands for left
        if root.right:
            self.recu_tree(root.right, prev_val + root.val, prev_path + [root.val])

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []
        self.recu_tree(root, 0, [])
        return self.sumval_node[target] if target in self.sumval_node.keys() else []