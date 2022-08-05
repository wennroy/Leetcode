# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        if not root:
            return []
        ans = []
        CurLevel = [root]
        depth = 1
        while True:
            nxtLevel, cur_ans = [], []

            for node in CurLevel:
                cur_ans.append(node.val)
                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            CurLevel = nxtLevel
            if depth == -1:
                cur_ans = cur_ans[::-1]
            depth *= -1
            if cur_ans:
                ans.append(cur_ans)
            else:
                break
        return ans

import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2: tmp.appendleft(node.val) # 偶数层 -> 队列头部
                else: tmp.append(node.val) # 奇数层 -> 队列尾部
                if node.left: deque.append(node.left)
                if node.right: deque.append(node.right)
            res.append(list(tmp))
        return res

# 作者：jyd
# 链接：https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。