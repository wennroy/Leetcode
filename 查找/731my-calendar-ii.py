# 线段树
'''
class Node:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        """
        left:   左孩子
        right:  右孩子
        val:    值
        lazy:   懒惰标记，是0说明没有懒惰标记，是正数说明这里的懒惰标记还未下放
        """
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy
    # 对于 __reor__ 的解释 https://www.pythontutorial.net/python-oop/python-__repr__/#:~:text=The%20__repr__%20method,returned%20string%20of%20the%20object_name.
    def __repr__(self):
        return f'<Node val: {self.val} lazy: {self.lazy} {self.left} {self.right}>'


class MySegTree:
    def __init__(self, size):
        """
        size:   线段树的总大小（根节点管理的区间的长度）
        """
        self.size = size
        self.root = Node()
        return

    def push_down(self, node, s, e):
        """
        向下更新，并传递懒惰更新标志
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        """
        mid = s + ((e - s) >> 1)  # >>位移一个bit
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if not node.lazy:
            return
        node.left.val += node.lazy
        node.right.val += node.lazy
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0
        return

    def push_up(self, node):
        """
        向上更新，要求node的两个子节点均已更新完
        node:   当前节点
        """
        node.val = max(node.left.val, node.right.val)
        return

    def update(self, node, s, e, l, r, add):
        """
        更新闭区间[l, r]，给此区间内的每个值，都加上add
        闭区间[l, r]和当前区间[s, e]的交集一定非空
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        l:      left，要更改的区间的左边界
        r:      right，要更改的区间的右边界
        add:    addition，增量
        """
        if l <= s and e <= r:
            node.val += add
            node.lazy += add
            return

        self.push_down(node, s, e)
        mid = s+((e-s)>>1)

        if l <= mid:
            self.update(node.left, s, mid, l, r, add)
        if r > mid:
            self.update(node.right, mid+1, e, l, r, add)

        self.push_up(node)
        return

    def query(self, node, s, e, l, r):
        """
        查询闭区间[l, r]的区间最大值
        闭区间[l, r]和当前区间[s, e]一定是有交集的
        node:   当前节点
        s:      start，当前节点管理的左边界（含）
        e:      end，当前节点管理的右边界（含）
        l:      left，要更改的区间的左边界
        r:      right，要更改的区间的右边界
        """
        if l <= s and e <= r:
            return node.val

        self.push_down(node, s, e)
        mid = s + ((e - s) >> 1)

        ans = float('-inf')
        if l <= mid:
            ans = max(ans, self.query(node.left, s, mid, l, r))
        if r > mid:
            ans = max(ans, self.query(node.right, mid + 1, e, l, r))

        return ans

class MyCalendarTwo:
    def __init__(self):
        self.size = 10 ** 9
        self.seg_tree = MySegTree(size=self.size)


    def book(self, start: int, end: int) -> bool:
        # 如果该时间段内任意时间片被预定超过2次说明无法预定当前请求
        if self.seg_tree.query(self.seg_tree.root, 0, self.size, start, end-1) >= 2:
            return False
        # 如果可以预定当前请求，为预定到的时间段内的每个时间片的占用次数+1
        self.seg_tree.update(self.seg_tree.root, 0, self.size, start, end-1, 1)
        return True

# 作者：isuxiz
# 链接：https://leetcode.cn/problems/my-calendar-ii/solution/by-isuxiz-o3jm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''
# 标答的线段树，利用数组存储会比树快很多

class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0])
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/my-calendar-ii/solution/wo-de-ri-cheng-an-pai-biao-ii-by-leetcod-wo6n/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

k = MyCalendarTwo()
k.book(10,20)
k.book(50,60)
k.book(10,40)
