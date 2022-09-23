# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from math import inf
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 递归求解
        def recur(root) -> [int, int]:
            # 返回两个值，左边的为当前结点最长的path sum，右边为当前节点下的最长path sum
            if not root:
                return [-inf, -inf]

            left_res, right_res = recur(root.left), recur(root.right)
            cur_max = max(left_res[0], right_res[0], 0) + root.val
            max_val = max(cur_max, left_res[1], right_res[1], left_res[0] + right_res[0] + root.val)
            return [cur_max, max_val]

        return recur(root)[1]

# 标答：基本一致
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / binary - tree - maximum - path - sum / solution / er - cha - shu - zhong - de - zui - da - lu - jing - he - by - leetcode - /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。