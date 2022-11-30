# 哈希表 + 有序数列
from collections import defaultdict
class FreqStack:

    def __init__(self):
        from sortedcontainers import SortedDict
        self.umap = defaultdict(int)
        self.count = SortedDict()

    def push(self, val: int) -> None:
        self.umap[val] += 1
        self.count.setdefault(self.umap[val], [])
        self.count[self.umap[val]].append(val)

    def pop(self) -> int:
        count = self.count.keys()[-1]
        val = self.count[count].pop()
        self.umap[val] -= 1
        if not self.count[count]:
            self.count.pop(count)

        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# 答案思路差不多，很类似
class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return val

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-frequency-stack/solution/zui-da-pin-lu-zhan-by-leetcode-solution-moay/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。