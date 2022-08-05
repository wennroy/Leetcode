# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # BFS
        if not root:
            return []
        ans = []
        CurLevel = [root]
        while CurLevel:
            nxtLevel = []
            for node in CurLevel:
                ans.append(node.val)
                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            CurLevel = nxtLevel
        return ans

# 层序BFS，可以直接维护一个队列
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return res

# 作者：jyd
# 链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/solution/mian-shi-ti-32-i-cong-shang-dao-xia-da-yin-er-ch-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。