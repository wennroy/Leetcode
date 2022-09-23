# 卡在一个用例出错了，思路有问题

class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self._head = ListNode(0)
        self._tail = self._head
        self._n = 0

    def get(self, index: int) -> int:
        if index >= self._n:
            return -1
        if index < self._n // 2:
            pt = self._head.next
            for _ in range(index):
                pt = pt.next
        else:
            pt = self._tail
            for _ in range(self._n - index - 1):
                pt = pt.prev
        return pt.val

    def addAtHead(self, val: int) -> None:
        pt, pt_next = self._head, self._head.next
        pt.next = ListNode(val, pt_next, self._head)
        if pt_next:
            pt_next.prev = pt.next
        self._n += 1
        if self._tail == self._head:
            self._tail = self._head.next
        return None

    def addAtTail(self, val: int) -> None:
        pt = self._tail
        pt.next = ListNode(val, None, pt)
        self._n += 1
        self._tail = pt.next
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self._n:
            self.addAtTail(val)
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index > self._n:
            return

        if index < self._n // 2:
            pt = self._head.next
            for _ in range(index):
                pt = pt.next
        else:
            pt = self._tail
            for _ in range(self._n - index - 1):
                pt = pt.prev
        pt_prev = pt.prev
        pt_prev.next = ListNode(val, pt, pt_prev)
        pt.prev = pt_prev.next
        self._n += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._n:
            return None

        if index == self._n - 1:
            self._tail = self._tail.prev
            self._tail.next = None
            return None

        if index < self._n // 2:
            pt = self._head.next
            for _ in range(index):
                pt = pt.next
        else:
            pt = self._tail
            for _ in range(self._n - index - 1):
                pt = pt.prev

        pt_prev, pt_next = pt.prev, pt.next
        pt_prev.next, pt_next.prev = pt_next, pt_prev
        self._n -= 1
        return None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# 单向链表
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode-solution-abix/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 同时需要Sentinel head and tail的双向链表
# 有很多地方很相似，但细节要细扣

class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
        return curr.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -= 1
        pred.next = succ
        succ.prev = pred

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-linked-list/solution/she-ji-lian-biao-by-leetcode-solution-abix/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。