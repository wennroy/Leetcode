# 哈希表写法
from collections import defaultdict
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptA, ptB = headA, headB
        record = defaultdict(int)
        while ptA:
            record[ptA] += 1
            ptA = ptA.next
        while ptB:
            if record[ptB] == 1:
                return ptB
            ptB = ptB.next
        return None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


# 作者：z1m
# 链接：https: // leetcode.cn / problems / liang - ge - lian - biao - de - di - yi - ge - gong - gong - jie - dian - lcof / solution / shuang - zhi - zhen - fa - lang - man - xiang - yu - by - ml - zimingm /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

