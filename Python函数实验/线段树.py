class Segment_tree:
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


# 含lazy下放
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