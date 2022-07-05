# Sorted后暴力遍历法
# 一个新知识，利用SortedDict可以保证Dict的keys()是保持排序的状态，然后进行遍历

# 需改进的点：Sorteddict就是为了方便二分查找而设计，在插入的过程应该使用二分查找而不是直接遍历
class MyCalendar:

    def __init__(self):
        from sortedcontainers import SortedDict
        self.record = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if not self.record:
            self.record[start] = end
            return True

        n = len(self.record.keys())
        last_val = self.record.keys()[0]

        if end <= last_val:
            self.record[start] = end
            return True

        for i in range(1, n):
            val = self.record.keys()[i]
            if end <= val:
                if start >= self.record[last_val]:
                    self.record[start] = end
                    return True
                else:
                    return False
            last_val = val

        if start >= self.record[last_val]:
            self.record[start] = end
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


'''
方法二：二分查找
'''

from sortedcontainers import SortedDict

class MyCalendar:
    def __init__(self):
        self.booked = SortedDict()

    def book(self, start: int, end: int) -> bool:
        i = self.booked.bisect_left(end)
        if i == 0 or self.booked.items()[i - 1][1] <= start:
            self.booked[start] = end
            return True
        return False

'''
方法三：线段树
'''
class MyCalendar:
    def __init__(self):
        self.tree = set()
        self.lazy = set()

    def query(self, start: int, end: int, l: int, r: int, idx: int) -> bool:
        if r < start or end < l:
            return False
        if idx in self.lazy:  # 如果该区间已被预订，则直接返回
            return True
        if start <= l and r <= end:
            return idx in self.tree
        mid = (l + r) // 2
        return self.query(start, end, l, mid, 2 * idx) or \
               self.query(start, end, mid + 1, r, 2 * idx + 1)

    def update(self, start: int, end: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree.add(idx)
            self.lazy.add(idx)
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, 2 * idx)
            self.update(start, end, mid + 1, r, 2 * idx + 1)
            self.tree.add(idx)
            if 2 * idx in self.lazy and 2 * idx + 1 in self.lazy:
                self.lazy.add(idx)

    def book(self, start: int, end: int) -> bool:
        if self.query(start, end - 1, 0, 10 ** 9, 1):
            return False
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return True

'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/my-calendar-i/solution/wo-de-ri-cheng-an-pai-biao-i-by-leetcode-nlxr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''