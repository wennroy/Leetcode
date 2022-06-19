'''
2022/06/19 船新版本
'''
from collections import Counter
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        pt = root
        stack = [pt]
        val_dict = defaultdict(int)
        val_dict[None] = 0
        while stack:
            pt = stack[-1]
            if pt.left and not pt.left in val_dict.keys():
                pt = pt.left
                stack.append(pt)
            elif pt.right and not pt.right in val_dict.keys():
                pt = pt.right
                stack.append(pt)
            else:
                val_dict[pt] = pt.val + val_dict[pt.left] + val_dict[pt.right]
                stack.pop()
        val_dict.pop(None)
        Counters = Counter(val_dict.values())
        ans = []
        for val, time in Counters.most_common():
            if ans == []:
                most_common_time = time
                ans.append(val)
            elif time == most_common_time:
                ans.append(val)
            else:
                break
        return ans


'''
2020/08/17
以前的版本
'''

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        self.record = {}
        def sumtree(self, root):
            if root == None:
                return 0
            self.record[root] = root.val + sumtree(self,root.left) + sumtree(self,root.right)
            return self.record[root]
        sumtree(self,root)
        ans= []
        k = Counter(self.record.values()).most_common()
        most_count = k[0][1]
        for i in k:
            if i[1] != most_count:
                break
            ans.append(i[0])

        return ans

'''
两个几乎完全一样的版本。一个利用stack存储指针点，一个利用递归来计算。
'''


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            sum = node.val + dfs(node.left) + dfs(node.right)
            cnt[sum] += 1
            return sum
        dfs(root)

        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]
'''
标答利用dfs，本质上也就是递归。相对于来说，少开销了一个dict的空间，利用list来简化。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/most-frequent-subtree-sum/solution/chu-xian-ci-shu-zui-duo-de-zi-shu-yuan-s-kdjc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''