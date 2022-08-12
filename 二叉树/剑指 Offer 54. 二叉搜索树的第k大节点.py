# 反向二叉树中序遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
        self.cnt = 0
    def in_order_traversal(self, root, k):
        if not root:
            return False
        self.in_order_traversal(root.right, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
            return
        elif self.cnt > k:
            return
        self.in_order_traversal(root.left, k)

        return

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.in_order_traversal(root,k)
        return self.ans


# 中序遍历

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)

        self.k = k
        dfs(root)
        return self.res

# 作者：jyd
# 链接：https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。