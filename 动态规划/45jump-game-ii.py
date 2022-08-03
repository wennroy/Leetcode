# 动态规划 动态规划由于每次需要考虑 i <= m = max(nums) 的步数，因此时间复杂度最大可能是
# O(nxm)，导致速度过慢
from math import inf
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            min_count = inf
            for j in range(nums[i]):
                if i+j+1 < n and dp[i+j+1] < min_count:
                    min_count = dp[i+j+1]
            dp[i] = min_count + 1
        return dp[0]

# 贪心 3636ms -> 44 ms 真正意义上的O(n^2)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。