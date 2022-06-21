# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        def dfs(self, root: TreeNode) -> list[int]:
            if not root.left and not root.right:
                return [root.val, 0]  # [val, level]
            elif not root.left:
                ans = dfs(self, root.right)
                return [ans[0], ans[1] + 1]

            elif not root.right:
                ans = dfs(self, root.left)
                return [ans[0], ans[1] + 1]
            else:
                ans_left, ans_right = dfs(self, root.left), dfs(self, root.right)
                if ans_left[1] >= ans_right[1]:
                    ans = ans_left
                else:
                    ans = ans_right

                return [ans[0], ans[1] + 1]

        return dfs(self, root)[0]

'''
标答DFS
'''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        curVal = curHeight = 0
        def dfs(node: Optional[TreeNode], height: int) -> None:
            if node is None:
                return
            height += 1
            dfs(node.left, height)
            dfs(node.right, height)
            nonlocal curVal, curHeight
            if height > curHeight:
                curHeight = height
                curVal = node.val
        dfs(root, 0)
        return curVal
'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/find-bottom-left-tree-value/solution/zhao-shu-zuo-xia-jiao-de-zhi-by-leetcode-weeh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            ans = node.val
        return ans

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/find-bottom-left-tree-value/solution/zhao-shu-zuo-xia-jiao-de-zhi-by-leetcode-weeh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''