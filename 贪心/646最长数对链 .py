# 类似于贪心的算法

from bisect import bisect_right
from bisect import bisect_left

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        from sortedcontainers import SortedDict
        record = SortedDict()
        for a, b in pairs:
            if a not in record.keys():
                record[a] = b
            elif record[a] > b:
                record[a] = b

        m = len(record.keys())
        dp = [0] * m
        dp[0] = 1
        for i in range(m):
            if i:
                dp[i] = max(dp[i - 1], dp[i])
            nxt_idx = bisect_right(record.keys(), record[record.keys()[i]])
            if nxt_idx < m:
                dp[nxt_idx] = max(dp[nxt_idx], dp[i] + 1)

        return max(dp)

# 最长递增子序列
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        arr = []
        for x, y in pairs:
            i = bisect_left(arr, x)
            if i < len(arr):
                arr[i] = min(arr[i], y)
            else:
                arr.append(y)
        return len(arr)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-length-of-pair-chain/solution/zui-chang-shu-dui-lian-by-leetcode-solut-ifpn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 贪心
from math import inf
class Solution(object):
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-length-of-pair-chain/solution/zui-chang-shu-dui-lian-by-leetcode-solut-ifpn/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。