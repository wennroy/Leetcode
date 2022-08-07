# 暴力记忆化搜索

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        from functools import lru_cache
        @lru_cache(None)
        def validPart(i):
            if i >= n:
                return True

            if i < n - 1 and nums[i] == nums[i + 1] and validPart(i + 2):
                return True
            if i < n - 2 and nums[i] == nums[i + 1] == nums[i + 2] and validPart(i + 3):
                return True
            if i < n - 2 and nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1] == 1 and validPart(i + 3):
                return True

            return False

        return validPart(0)

# 更新一个DP动态规划算法，能记忆化搜索，看来就能动态规划，
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums):
            if i > 0 and f[i - 1] and x == nums[i - 1] or \
               i > 1 and f[i - 2] and (x == nums[i - 1] == nums[i - 2] or
                                       x == nums[i - 1] + 1 == nums[i - 2] + 2):
               f[i + 1] = True
        return f[n]

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/solution/by-endlesscheng-8y73/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。