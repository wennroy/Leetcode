# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_idx = max(range(len(nums)), key=nums.__getitem__)
        head = TreeNode(val = nums[max_idx], left = self.constructMaximumBinaryTree(nums[:max_idx]), right = self.constructMaximumBinaryTree(nums[max_idx+1:]))
        return head


# 单调栈，先扫描一遍所有的值，最大值左侧的数组部分下放到该节点的左子节点，右侧的数组部分下放到该节点的右子节点；

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stk = list()
        left, right = [-1] * n, [-1] * n
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        root = None
        for i in range(n):
            if left[i] == right[i] == -1:
                root = tree[i]
            elif right[i] == -1 or (left[i] != -1 and nums[left[i]] < nums[right[i]]):
                tree[left[i]].right = tree[i]
            else:
                tree[right[i]].left = tree[i]

        return root


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / maximum - binary - tree / solution / zui - da - er - cha - shu - by - leetcode - solution - lbeo /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 我们还可以把最后构造树的过程放进单调栈求解的步骤中，省去用来存储左右边界的数组。下面的代码理解起来较为困难，同一个节点的左右子树会被多次赋值，读者可以仔细品味其妙处所在。
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stk = list()
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                tree[i].left = tree[stk[-1]]
                stk.pop()
            if stk:
                tree[stk[-1]].right = tree[i]
            stk.append(i)

        return tree[stk[0]]


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-binary-tree/solution/zui-da-er-cha-shu-by-leetcode-solution-lbeo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。