# 栈遍历 + 交换

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            cur = TreeNode(val=val, left=root)
            return cur

        def addRowforRoot(root, val):
            left_root = root.left
            right_root = root.right
            root.left = TreeNode(val, left_root)
            root.right = TreeNode(val, right=right_root)

        root_stack, depth_stack = [root], [1]
        while root_stack:
            cur_root = root_stack.pop()
            cur_depth = depth_stack.pop()
            if cur_depth == depth - 1:
                addRowforRoot(cur_root, val)
                continue
            if cur_root.left:
                root_stack.append(cur_root.left)
                depth_stack.append(cur_depth + 1)
            if cur_root.right:
                root_stack.append(cur_root.right)
                depth_stack.append(cur_depth + 1)
        return root


# DFS
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if root == None:
            return
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root

# BFS
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root, None)
        curLevel = [root]
        for _ in range(1, depth - 1):
            tmpt = []
            for node in curLevel:
                if node.left:
                    tmpt.append(node.left)
                if node.right:
                    tmpt.append(node.right)
            curLevel = tmpt
        for node in curLevel:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/add-one-row-to-tree/solution/zai-er-cha-shu-zhong-zeng-jia-yi-xing-by-xcaf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。