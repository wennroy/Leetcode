# 为了周赛写的较为复杂版本
# 当时在考虑 7&4 = 4所以在确保7是不是也能纳入范围。
# 耗时和空间都比较大
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0]] * n
        dp[0] = [nums[0], 1]
        for i in range(1, n):
            if (dp[i - 1][0] & nums[i]) >= nums[i]:
                dp[i] = [(dp[i - 1][0] & nums[i]), 1 + dp[i - 1][1]]
            else:
                dp[i] = [nums[i], 1]

        dp.sort(key=lambda x: (-x[0], -x[1]))
        # print(dp)
        return dp[0][1]

# 正常的解法，直接遍历
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = cnt = 0
        for x in nums:
            if x == mx:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-subarray-with-maximum-bitwise-and/solution/nao-jin-ji-zhuan-wan-by-endlesscheng-75dq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。