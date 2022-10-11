# 并查集复杂做法
from typing import List, Optional
from collections import Counter
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # 并查集，把连接在一起的组件放一起就完事了
        pt = head
        n = 0
        while pt:
            n += 1
            pt = pt.next
        parent = [-1] * n
        if n == 1:
            return 1

        # 最简单的并查集
        def find(x):
            if parent[x] == -1 or x == -1:
                return -1
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def update(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if px == -1 or py == -1:
                return
            parent[px] = py
            return

        for num in nums:
            parent[num] = num
        # print(parent)
        pt = head
        last = pt.val
        pt = pt.next
        while pt:
            update(last, pt.val)
            last = pt.val
            pt = pt.next

        parent_list = list(map(find, parent))
        cnt = Counter(parent_list)
        if -1 in cnt.keys():
            return len(cnt) - 1
        else:
            return len(cnt)


# 哈希表直接写就完事了
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        numsSet = set(nums)
        inSet = False
        res = 0
        while head:
            if head.val not in numsSet:
                inSet = False
            elif not inSet:
                inSet = True
                res += 1
            head = head.next
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/linked-list-components/solution/lian-biao-zu-jian-by-leetcode-solution-5f91/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。