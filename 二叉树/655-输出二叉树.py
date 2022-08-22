# BFS完直接DFS
# 给你一棵二叉树的根节点 root ，请你构造一个下标从 0 开始、大小为 m x n 的字符串矩阵 res ，用以表示树的 格式化布局 。构造此格式化布局矩阵需要遵循以下规则：
# 树的 高度 为 height ，矩阵的行数 m 应该等于 height + 1 。
# 矩阵的列数 n 应该等于 2height+1 - 1 。
# 根节点 需要放置在 顶行 的 正中间 ，对应位置为 res[0][(n-1)/2] 。
# 对于放置在矩阵中的每个节点，设对应位置为 res[r][c] ，将其左子节点放置在 res[r+1][c-2height-r-1] ，右子节点放置在 res[r+1][c+2height-r-1] 。
# 继续这一过程，直到树中的所有节点都妥善放置。
# 任意空单元格都应该包含空字符串 "" 。
# 返回构造得到的矩阵 res 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/print-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def depth(root):
            nxtLevel = [root]
            ans = -1
            while nxtLevel:
                ans += 1
                curLevel = nxtLevel
                nxtLevel = []
                for node in curLevel:
                    if node.left:
                        nxtLevel.append(node.left)
                    if node.right:
                        nxtLevel.append(node.right)

            return ans

        height = depth(root)
        n, m = 2 ** (height + 1) - 1, height + 1
        res = [[""] * n for _ in range(m)]

        def dfs(root, row, col):
            if not root:
                return
            res[row][col] = str(root.val)
            if root.left:
                dfs(root.left, row + 1, col - 2 ** (height - row - 1))
            if root.right:
                dfs(root.right, row + 1, col + 2 ** (height - row - 1))
            return

        dfs(root, 0, (n - 1) // 2)
        return res