# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 在链表上进行排序，插入排序
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # 看来O(n2)能过，那就先写个O(n2)，空间复杂度O(1)
#         def insert_before_list(last_list: Optional[ListNode], insert_list: Optional[ListNode]) -> None:
#             last.next = insert_list.next
#             if not last_list:
#                 insert_list.next = head
#             else:
#                 insert_list.next = last_list.next
#                 last_list.next = insert_list
#         if not head:
#             return None
#         cur_pt = head.next
#         last = head
#         while cur_pt:
#             val = cur_pt.val
#             if last.val <= val:
#                 last = cur_pt
#                 cur_pt = cur_pt.next
#                 continue
#
#             elif head.val > val:
#                 insert_before_list(None, cur_pt)
#                 head = cur_pt
#                 cur_pt = last
#             else:
#                 sec_pt = head
#                 while sec_pt != last:
#                     if val <= sec_pt.next.val:
#                         insert_before_list(sec_pt, cur_pt)
#                         break
#                     sec_pt = sec_pt.next
#             last = cur_pt
#             cur_pt = cur_pt.next
#
#         return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummyHead.next

    def swap(self, head1, head2) -> None:
        h1_next_next, h2_next_next = head1.next.next, head2.next.next
        h1_next, h2_next = head1.next, head2.next
        head1.next, head2.next = h2_next, h1_next
        h1_next.next, h2_next.next = h2_next_next, h1_next_next
        return None

    def mergesort(self, head, tail, n):
        if n <= 2:
            if head.next.val > tail.next.val:
                self.swap(head, tail)
            return head
        mid = n // 2
        count = 1
        mid_pt = head
        while count < mid:
            mid_pt = mid_pt.next
            count += 1
        head1 = self.mergesort(head, mid_pt, count)
        head2 = self.mergesort(mid_pt.next, tail, n - count)
        self.merge(head1, head2)
        return head1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        n = 1
        dummyHead = ListNode(0, head)
        pt = dummyHead
        while pt.next.next:
            n += 1
            pt = pt.next
        print(n, pt.val)
        return self.mergesort(dummyHead, pt, n).next


# 递归
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

# 作者：jyd
# 链接：https://leetcode.cn/problems/sort-list/solution/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':
    sol = Solution()

    def print_list(head: Optional[ListNode]):
        if not head:
            return None
        pt = head
        visited = set()
        ans = []
        while pt:
            if pt in visited:
                print(ans)
                raise RecursionError('Found a loop in list.')
            ans.append(pt.val)
            visited.add(pt)
            pt = pt.next
        return ans


    head = ListNode(4)
    pt = head
    pt.next = ListNode(2)
    pt = pt.next
    pt.next = ListNode(1)
    pt = pt.next
    pt.next = ListNode(3)
    pt = pt.next
    pt.next = ListNode(5)
    pt = pt.next

    sol.sortList(head)