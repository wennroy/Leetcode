# 利用deque来维护一个queue队列

# 由于from queue import Queue 过于难用，所以选取了deque来完成
# deque对于list的好处：list在popleft的时候，基本上是元素的位移，会导致O(n)的时间复杂度，而deque不会。
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.qsize = 0

    def next(self, val: int) -> float:
        if self.qsize == self.size:
            self.sum -= self.queue.popleft()
            self.sum += val
            self.queue.append(val)
            return self.sum / self.size
        else:
            self.sum += val
            self.queue.append(val)
            self.qsize += 1
            return self.sum / self.qsize

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.q = deque()

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.sum += val
        self.q.append(val)
        return self.sum / len(self.q)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/qIsx9U/solution/hua-dong-chuang-kou-de-ping-jun-zhi-by-l-0rxf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。