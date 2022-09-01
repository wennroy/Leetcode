# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 构建无向图
        vectors = defaultdict(list)
        nxtLevel = [root]
        while nxtLevel:
            curLevel = nxtLevel
            nxtLevel = []
            for node in curLevel:
                if node.left:
                    vectors[node].append(node.left)
                    vectors[node.left].append(node)
                    nxtLevel.append(node.left)
                if node.right:
                    vectors[node].append(node.right)
                    vectors[node.right].append(node)
                    nxtLevel.append(node.right)
        ans = 0
        visited = defaultdict(lambda: False)

        # 寻找最长路径
        def dfs(node: TreeNode, val: int) -> int:
            '''
            Input:
            node: 输入当前的遍历到的结点
            val: 当前遍历轮次的值
            count: 计算已经出现的次数

            Output:
            返回该数字最长的出现次数
            '''
            nonlocal ans
            largest_count = sec_large_count = 0
            visited[node] = True
            for i, nxt_node in enumerate(vectors[node]):
                if nxt_node.val == node.val and not visited[nxt_node]:
                    cur_count = dfs(nxt_node, val)
                    if cur_count >= largest_count:
                        largest_count, sec_large_count = cur_count, largest_count
                    elif cur_count > sec_large_count:
                        sec_large_count = cur_count
            return sec_large_count + largest_count + 1

        for node in vectors.keys():
            if not visited[node]:
                cur_ans = dfs(node, node.val)
                print(cur_ans)
                if cur_ans > ans:
                    ans = cur_ans

        return ans - 1 if vectors else 0


if __name__ == '__main__':
    head = TreeNode(4)
    sol = Solution()
    print(sol.longestUnivaluePath(head))


# 标答DFS 脑子突然抽了写不出来？？？？
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left1 = left + 1 if node.left and node.left.val == node.val else 0
            right1 = right + 1 if node.right and node.right.val == node.val else 0
            nonlocal ans
            ans = max(ans, left1 + right1)
            return max(left1, right1)
        dfs(root)
        return ans