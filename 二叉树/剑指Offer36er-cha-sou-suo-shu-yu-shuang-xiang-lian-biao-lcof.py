"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# 中序遍历

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        node_list = []

        def in_order_traversal(root):
            if not root:
                return

            in_order_traversal(root.left)
            node_list.append(root)
            in_order_traversal(root.right)
            return

        in_order_traversal(root)
        for i in range(1, len(node_list)):
            node_list[i - 1].right = node_list[i]
            node_list[i].left = node_list[i - 1]

        node_list[-1].right = node_list[0]
        node_list[0].left = node_list[-1]

        return node_list[0]