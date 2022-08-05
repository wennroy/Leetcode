class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        record = {}
        first = 1
        for a in s:
            if not a in record:
                record[a] = first
                first += 1
            else:
                record[a] = 0

        min_first = 50001
        for (key, val) in record.items():
            if val != 0 and val < min_first:
                min_first = val
                ans = key
        return ans if min_first != 50001 else ' '

# 几乎一样的标答操作，记录存储索引
class Solution:
    def firstUniqChar(self, s: str) -> str:
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        return ' ' if first == n else s[first]

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-by-3zqv5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 利用collections.Counter计算
import collections

class Solution:
    def firstUniqChar(self, s: str) -> str:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return ch
        return ' '

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-by-3zqv5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。