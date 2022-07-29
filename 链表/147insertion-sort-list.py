# 在148用插入排序过不了，你点的插入排序，放到147过了


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 看来O(n2)能过，那就先写个O(n2)，空间复杂度O(1)
        def insert_before_list(last_list: Optional[ListNode], insert_list: Optional[ListNode]) -> None:
            last.next = insert_list.next
            if not last_list:
                insert_list.next = head
            else:
                insert_list.next = last_list.next
                last_list.next = insert_list
        if not head:
            return None
        cur_pt = head.next
        last = head
        while cur_pt:
            val = cur_pt.val
            if last.val <= val:
                last = cur_pt
                cur_pt = cur_pt.next
                continue

            elif head.val > val:
                insert_before_list(None, cur_pt)
                head = cur_pt
                cur_pt = last
            else:
                sec_pt = head
                while sec_pt != last:
                    if val <= sec_pt.next.val:
                        insert_before_list(sec_pt, cur_pt)
                        break
                    sec_pt = sec_pt.next
            last = cur_pt
            cur_pt = cur_pt.next

        return head

# 官方的解法好简洁啊
# 一个小技巧，利用Dummyhead来避免当前一个节点是None的时候，需要和None节点交换的问题，减少代码判断量。

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next


# 作者：LeetCode - Solution
# 链接：https://leetcode.cn/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。