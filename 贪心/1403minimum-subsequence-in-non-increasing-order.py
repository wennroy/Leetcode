class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        sum_of_nums = sum(nums)
        ans, ans_sum = [], 0
        for i in range(len(nums) - 1, -1, -1):
            ans.append(nums[i])
            ans_sum += nums[i]
            if 2 * ans_sum > sum_of_nums:
                return ans
