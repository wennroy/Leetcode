from typing import List
# 动态规划，看了提示才会写
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            cond1 = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            cond2 = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]

            if cond1 and cond2:
                res = min(dp[i - 1][0], dp[i - 1][1])
                dp[i][0] = res
                dp[i][1] = res + 1
            elif cond1:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
            else:
                dp[i][0] = dp[i - 1][1]
                dp[i][1] = dp[i - 1][0] + 1

        return min(dp[n - 1])

# 标答动态规划
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = 0, 1
        for i in range(1, n):
            at, bt = a, b
            a = b = n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                a = min(a, at)
                b = min(b, bt + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                a = min(a, bt)
                b = min(b, at + 1)
        return min(a, b)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/solution/shi-xu-lie-di-zeng-de-zui-xiao-jiao-huan-ux2y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from itertools import pairwise
from math import inf

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        not_swap, swap = 0, 1
        for (a1, b1), (a2, b2) in pairwise(zip(nums1, nums2)):  # 3.10 from itertools import pairwise
            ns = s = inf
            if a1 < a2 and b1 < b2:
                ns, s = not_swap, swap + 1
            if b1 < a2 and a1 < b2:
                ns, s = min(ns, swap), min(s, not_swap + 1)
            not_swap, swap = ns, s
        return min(not_swap, swap)

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/solution/dong-tai-gui-hua-kao-lu-xiang-lin-yuan-s-ni0p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。