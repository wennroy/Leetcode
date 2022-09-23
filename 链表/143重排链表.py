# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
from typing import Optional, List

class Solution:
    def insertNode(self, head: ListNode, tail: Optional[ListNode]) -> None:
        # tail结点需连结在head结点的下一个，也就是讲tail插入到head.next。
        # 由于tail是最后一个结点，我们不需要额外的考虑
        head_next = head.next
        head.next = tail
        tail.next = head_next
        return None

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pt = head
        q = deque()
        while pt:
            q.append(pt)
            pt = pt.next

        while len(q) > 1:
            head, tail = q.popleft(), q.pop()
            if q:
                q[-1].next = None
            else:
                head.next = None
            self.insertNode(head, tail)
        if q:
            last = q.pop()
            last.next = None
        return None


# 差不多一样的思路
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        vec = list()
        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1

        vec[i].next = None


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / reorder - list / solution / zhong - pai - lian - biao - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。