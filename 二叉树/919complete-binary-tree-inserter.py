# 老老实实拿tree structure来写了emm
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = root
        def count_dfs(root: TreeNode) -> int:
            if not root:
                return 0
            return count_dfs(root.left) + count_dfs(root.right) + 1
        self.idx = count_dfs(root)

    def insert(self, val: int) -> int:
        self.idx += 1
        idx = self.idx
        path = []  # 0 stands for left, 1 stands for right
        if idx % 2:
            last = 1
        else:
            last = 0
        idx = idx // 2
        while idx != 1:
            if idx % 2:
                path.append(1)
            else:
                path.append(0)
            idx = idx // 2
        pt = self.tree
        while path:
            if path.pop():
                pt = pt.right
            else:
                pt = pt.left
        father_val = pt.val
        if last:
            pt.right = TreeNode(val)
        else:
            pt.left = TreeNode(val)
        return father_val

    def get_root(self) -> TreeNode:
        return self.tree


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

# 队列
from collections import deque

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = deque()

        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if not (node.left and node.right):
                self.candidate.append(node)

    def insert(self, val: int) -> int:
        candidate_ = self.candidate

        child = TreeNode(val)
        node = candidate_[0]
        ret = node.val

        if not node.left:
            node.left = child
        else:
            node.right = child
            candidate_.popleft()

        candidate_.append(child)
        return ret

    def get_root(self) -> TreeNode:
        return self.root

# 二进制
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.cnt = 0

        q = deque([root])
        while q:
            self.cnt += 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        self.cnt += 1

        child = TreeNode(val)
        node = self.root
        highbit = self.cnt.bit_length() - 1

        for i in range(highbit - 1, 0, -1):
            if self.cnt & (1 << i):
                node = node.right
            else:
                node = node.left

        if self.cnt & 1:
            node.right = child
        else:
            node.left = child

        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / complete - binary - tree - inserter / solution / wan - quan - er - cha - shu - cha - ru - qi - by - leetcod - lf8t /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。