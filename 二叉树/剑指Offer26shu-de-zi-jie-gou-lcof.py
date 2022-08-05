# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False

        def isTheSame(A, B):
            if not B:
                return True
            if not A:
                return False

            if A.val != B.val:
                return False

            if isTheSame(A.left, B.left) and isTheSame(A.right, B.right):
                return True

        stack = [A]
        while stack:
            cur_root = stack.pop()
            if isTheSame(cur_root, B):
                return True
            if cur_root.left:
                stack.append(cur_root.left)
            if cur_root.right:
                stack.append(cur_root.right)

        return False


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

# 作者：jyd
# 链接：https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/solution/mian-shi-ti-26-shu-de-zi-jie-gou-xian-xu-bian-li-p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。