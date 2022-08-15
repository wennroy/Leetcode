# 利用栈记录路过的所有结点，然后利用结点靠近来判断


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pt = root
        stack = []
        while pt != p:
            stack.append(pt)
            if pt.val < p.val:
                pt = pt.right
            else:
                pt = pt.left
        stack.append(pt)
        left_pt = right_pt = None
        left_val = -math.inf
        right_val = math.inf
        left = -1
        right = len(stack)

        for i, cur_pt in enumerate(stack[::-1]):
            if cur_pt == q:
                return cur_pt
            if left_val < cur_pt.val and cur_pt.val < q.val:
                left_val = cur_pt.val
                left_pt = cur_pt
                left = i
            elif right_val > cur_pt.val and cur_pt.val > q.val:
                right_val = cur_pt.val
                right_pt = cur_pt
                right = i
        if left == -1:
            return right_pt
        elif right == len(stack):
            return left_pt
        else:
            return left_pt if left < right else right_pt


# 递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

# 一次遍历，第一次处于值中间即可

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/er-cha-sou-suo-shu-de-zui-jin-gong-gong-0wpw1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。