# 回家等通知写法
from collections import defaultdict
class Skiplist:

    def __init__(self):
        self.record = defaultdict(int)

    def search(self, target: int) -> bool:
        if target in self.record.keys():
            return True
        else:
            return False

    def add(self, num: int) -> None:
        self.record[num] += 1


    def erase(self, num: int) -> bool:
        self.record[num] -= 1
        if self.record[num] < 0:
            self.record.pop(num)
            return False
        else:
            if self.record[num] == 0:
                self.record.pop(num)
            return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

# https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf


# 大佬写法
from math import *

MAXLVL = 16
class SkiplistNode:
    def __init__(self, level, val):
        self.val = val
        self.levels = [None]*level

class Skiplist:
    def __init__(self):
        self.senhead = SkiplistNode(MAXLVL, -inf)

    def get_prev_lt(self, val):
        prev_nodes = [None] * MAXLVL
        x = self.senhead
        for i in reversed(range(MAXLVL)):
            while x and x.val < val:
                prvx, x = x, x.levels[i]
            prev_nodes[i] = x = prvx
        return prev_nodes

    def search(self, val):
        x = self.get_prev_lt(val)[0].levels[0]
        return x is not None and x.val == val

    def add(self, val):
        prev_nodes = self.get_prev_lt(val)
        newnode_level = min(1-int(log(1/random.random(), 0.5)), MAXLVL)
        x = SkiplistNode(newnode_level, val)
        for i in range(newnode_level):
            x.levels[i] = prev_nodes[i].levels[i]
            prev_nodes[i].levels[i] = x

    def erase(self, val):
        prev_nodes = self.get_prev_lt(val)
        x = prev_nodes[0].levels[0]
        if x is None or x.val > val: return False
        for i in range(len(x.levels)):
            prev_nodes[i].levels[i] = x.levels[i]
        return True

# 作者：migeater
# 链接：https://leetcode.cn/problems/design-skiplist/solution/san-ge-han-shu-by-migeater-rtcf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import random

MAX_LEVEL = 32
P_FACTOR = 0.25

def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv

class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level

class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        # 检测当前元素的值是否等于 target
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # 对第 i 层的状态进行更新，将当前元素的 forward 指向新的节点
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # 值不存在
            return False
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            # 对第 i 层的状态进行更新，将 forward 指向被删除节点的下一跳
            update[i].forward[i] = curr.forward[i]
        # 更新当前的 level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/design-skiplist/solution/she-ji-tiao-biao-by-leetcode-solution-e8yh/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。