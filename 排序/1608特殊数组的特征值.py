# 我这写的什么玩意儿？？？
from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        m = min(len(nums), max(nums))
        if m <= 0:
            return -1
        arr = [0] * (m + 1)
        first = True
        for i in range(n - 1, -1, -1):
            if nums[i] <= m:
                arr[nums[i]] = n - i
                if first:
                    val = n - i - 1
                    first = False
        if nums[i] > m:
            arr[-1] = n
            val = n - 1
        for i in range(m, 0, -1):
            if arr[i]:
                val = arr[i]
            if val == i:
                return i

        return -1

# 直接暴力
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/special-array-with-x-elements-greater-than-or-equal-x/solution/te-shu-shu-zu-de-te-zheng-zhi-by-leetcod-9wfo/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。