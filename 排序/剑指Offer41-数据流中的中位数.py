from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        return None

    def findMedian(self) -> float:
        n = self.arr.__len__()
        if n % 2 == 0:
            return (self.arr[n//2-1] + self.arr[n//2]) / 2
        return self.arr[(n-1)//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
import heapq

# 优先队列
class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / shu - ju - liu - zhong - de - zhong - wei - shu - lcof / solution / shu - ju - liu - zhong - de - zhong - wei - shu - by - lee - um4f /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 有序集合和双指针
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.lst = SortedList()
        self.left, self.right, self.left_value, self.right_value = 0, 0, None, None

    def addNum(self, num: int) -> None:
        n = len(self.lst)
        self.lst.add(num)
        if n != 0:
            if n & 1: self.right += 1
            else: self.left += 1
        self.left_value, self.right_value = self.lst[self.left], self.lst[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value)/2