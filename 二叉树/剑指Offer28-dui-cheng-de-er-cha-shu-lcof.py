# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def istwonodesSymmetric(A, B):
            if not A and not B:
                return True
            if not A:
                return False
            if not B:
                return False

            if A.val != B.val:
                return False

            if istwonodesSymmetric(A.left, B.right) and istwonodesSymmetric(A.right, B.left):
                return True
            return False

        return istwonodesSymmetric(root.left, root.right)

# 大佬就是写得简洁
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True

# 作者：jyd
# 链接：https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。