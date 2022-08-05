class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_range = [0] * 101
        for num in nums:
            nums_range[num] += 1
        ans = 0
        for i in range(1,101):
            if nums_range[i] > 0:
                ans += 1
        return ans

