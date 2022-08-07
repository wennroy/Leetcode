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