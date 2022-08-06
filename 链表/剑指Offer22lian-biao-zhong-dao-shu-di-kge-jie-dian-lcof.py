# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from collections import deque
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        q = deque()
        pt = head
        count = 0
        while pt:
            if count == k:
                q.append(pt)
                q.popleft()
            else:
                q.append(pt)
                count += 1
            pt = pt.next

        return q[0]


# 双指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        left = right = head
        for _ in range(k):
            right = right.next

        # right事实上位于None的位置，因此left会多走一格。
        while right:
            right = right.next
            left = left.next

        return left