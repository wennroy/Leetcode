from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start, end, l, r, idx, lazy) -> None:
        # lazy为下放的值
        if r < start or l > end:
            if lazy:
                self.tree[idx] = lazy
                self.lazy[idx] = lazy
            return
        if start <= l and r <= end and 2*idx not in self.tree.keys() and 2*idx+1 not in self.tree.keys():
            self.lazy[idx] += lazy + 1
            self.tree[idx] += lazy + 1    # 当前节点的数值储存
            # print(start, end, l, r, self.tree[idx], self.lazy[idx], lazy)
        else:
            mid = (l + r) // 2
            self.lazy[idx] += lazy
            self.update(start, end, l, mid, 2*idx, self.lazy[idx])
            self.update(start, end, mid+1, r, 2*idx+1, self.lazy[idx])
            self.lazy[idx] = 0
            self.tree[idx] = max(self.tree[2*idx], self.tree[2*idx+1])
        # if self.tree[idx] == 3:
        #     print(l,r,idx,lazy,self.lazy[idx])
        return

    def book(self, start: int, end: int) -> int:
        self.update(start, end-1, 0, 10**9, 1, 0)
        return self.tree[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

# 该题特殊情况导致，我们不需要下放lazy
# 在该节点中，出现最多次的一定是lazy+左右tree的值，所以就不需要lazy下放了

class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/my-calendar-iii/solution/wo-de-ri-cheng-an-pai-biao-iii-by-leetco-9rif/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法二：差分数组
from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = maxBook = 0
        for freq in self.d.values():
            maxBook += freq
            ans = max(ans, maxBook)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/my-calendar-iii/solution/wo-de-ri-cheng-an-pai-biao-iii-by-leetco-9rif/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。