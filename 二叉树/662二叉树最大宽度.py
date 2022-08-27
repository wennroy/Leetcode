# 简单BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
import math

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nxtLevel = defaultdict(int)
        max_width = 1
        nxtLevel[root] = 1
        while nxtLevel:
            curLevel = nxtLevel
            nxtLevel = defaultdict(int)
            left, right = math.inf, 0
            for node, val in curLevel.items():
                if val < left:
                    left = val
                if val > right:
                    right = val
                if node.left:
                    nxtLevel[node.left] = val * 2 - 1
                if node.right:
                    nxtLevel[node.right] = val * 2
            if right - left + 1 > max_width:
                max_width = right - left + 1

        return max_width

# BFS，直接用数据存储更快。
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        arr = [[root, 1]]
        while arr:
            tmp = []
            for node, index in arr:
                if node.left:
                    tmp.append([node.left, index * 2])
                if node.right:
                    tmp.append([node.right, index * 2 + 1])
            res = max(res, arr[-1][1] - arr[0][1] + 1)
            arr = tmp
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-width-of-binary-tree/solution/er-cha-shu-zui-da-kuan-du-by-leetcode-so-9zp3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 双端链表
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(root, 1)])
        max_wide = 1
        while dq:
            max_wide = max(dq[-1][1] - dq[0][1] + 1, max_wide)
            for _ in range(len(dq)):
                node, index = dq.popleft()
                if node.left:
                    dq.append((node.left, index * 2))
                if node.right:
                    dq.append((node.right, index * 2 + 1))
        return max_wide