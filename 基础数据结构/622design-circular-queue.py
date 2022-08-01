# 链表写法，但感觉不是特别快
class Node:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.next = nxt


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = Node()
        pt = self.head
        for i in range(k-1):
            pt.next = Node()
            pt = pt.next
        pt.next = Node()
        pt = pt.next
        pt.next = self.head
        self.tail = pt
        self.tail_pt = pt

    def enQueue(self, value: int) -> bool:
        if self.tail.next == self.tail_pt:
            return False
        self.tail = self.tail.next
        self.tail.val = value
        return True

    def deQueue(self) -> bool:
        if self.head == self.tail.next:
            return False
        self.head = self.head.next
        self.tail_pt = self.tail_pt.next
        return True

    def Front(self) -> int:
        if self.head == self.tail.next:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.head == self.tail.next:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return True if self.head == self.tail.next else False

    def isFull(self) -> bool:
        return True if self.tail.next == self.tail_pt else False


# 标答链表
class MyCircularQueue:
    def __init__(self, k: int):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = ListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-circular-queue/solution/she-ji-xun-huan-dui-lie-by-leetcode-solu-1w0a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# 数组做法

class MyCircularQueue:
    def __init__(self, k: int):
        self.front = self.rear = 0
        self.elements = [0] * (k + 1)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % len(self.elements)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.elements)
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.elements[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.elements[(self.rear - 1) % len(self.elements)]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.elements) == self.front

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-circular-queue/solution/she-ji-xun-huan-dui-lie-by-leetcode-solu-1w0a/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。