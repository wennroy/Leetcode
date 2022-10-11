import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            self.min_heap.append(num)
            return
        if not self.max_heap:
            if self.min_heap[0] >= num:
                self.max_heap.append(-num)
            else:
                self.max_heap.append(-self.min_heap.pop())
                self.min_heap.append(num)
            return

        if num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        n1, n2 = len(self.min_heap), len(self.max_heap)
        if n2 == 0:
            return float(self.min_heap[0])
        while abs(n1-n2) >= 2:
            if n1 > n2:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                n1 -= 1
                n2 += 1
            else:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                n1 += 1
                n2 -= 1
        if n1 == n2:
            ans = (self.min_heap[0] - self.max_heap[0]) / 2
        elif n1 > n2:
            ans = self.min_heap[0]
        else:
            ans = -self.max_heap[0]

        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 标答的优先队列
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
# 链接：https: // leetcode.cn / problems / find - median -from-data - stream / solution / shu - ju - liu - de - zhong - wei - shu - by - leetcode - ktkst /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。