# 经典头尾双指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:

            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [nums[left], nums[right]]

        return []